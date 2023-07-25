#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import argparse
import enum
from typing import Optional, List
import subprocess

class Action(enum.Enum):
    RUN = 1
    CLEAN = 2

class TocMaker:
    @staticmethod
    def __only_hashtags(x: str) -> bool:
        return len(x) == x.count("#") and len(x) > 0

    # generate md link for the text
    @staticmethod
    def __get_md_link(title: Optional[str]) -> str:
        if title is None:
            return ""
        title = title.lstrip(" #").rstrip()
        title = title.lower()
        out = ''
        for c in title:
            if c == ' ' or c == '-':
                out += '-'
            elif c == '_':
                out += '_'
            elif c.isalnum():
                out += c
        return out

    @staticmethod
    def __get_level(line: str) -> int:
        return len(line.split(" ")[0])

    @staticmethod
    def __get_content(line: str) -> str:
        return " ".join(line.split(" ")[1:])

    @staticmethod
    def __remove_code_fences(content: str) -> str:
        regex = r"^```.*?```\n"
        return re.sub(regex, "", content, 0, re.MULTILINE | re.DOTALL)


    @staticmethod
    def execute(content: str) -> str:
        content = TocMaker.__remove_code_fences(content)

        lines = content.split("\n")
        disable_tag = "[]()"
        lines = [line for line in lines if TocMaker.__only_hashtags(line.split(" ")[0]) and line.find(disable_tag) == -1]

        min_level = 1
        toc_lines = []
        for line in lines:
            level = (TocMaker.__get_level(line) - 1) - min_level
            if level < 0:
                continue
            text = "  " * level + "- [" + TocMaker.__get_content(line) + "](#" + TocMaker.__get_md_link(line) + ")"
            toc_lines.append(text)
        toc_text = "\n".join(toc_lines)
        return toc_text

class Toc:
    @staticmethod
    def execute(content: str, action: Action = Action.RUN) -> str:
        regex = r"\[\]\(toc\)\n" + r"(.*?)"+ r"\[\]\(toc\)"
        if action == Action.RUN:
            new_toc = TocMaker.execute(content)
            subst = r"[](toc)\n\n" + new_toc + r"\n[](toc)"
        else:
            subst = r"[](toc)\n[](toc)"
        return re.sub(regex, subst, content, 0, re.MULTILINE | re.DOTALL)



class Load:

    @staticmethod
    def extract_between_tags(content, tag):
        regex = r"\[\[" + tag + r"\]\].*?^(.*)^[\S ]*\[\[" + tag + r"\]\]"
        matches = re.finditer(regex, content, re.MULTILINE | re.DOTALL)
        for match in matches:
            return match.group(1)
        return ""

    @staticmethod
    def execute(content: str, action: Action = Action.RUN) -> str:
        new_content = ""
        last = 0

        regex = r"\[\]\(load\)\[\]\((.+?)\)\[\]\((.*?)\)\n(.*?)\[\]\(load\)"
        matches = re.finditer(regex, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            path = match.group(1)
            tags = match.group(2)
            words: List[str] = tags.split(":")

            fenced: List[str] = [tag for tag in words if tag.startswith("fenced")]
            words = [tag for tag in words if not tag.startswith("fenced")]

            filter: List[str] = [tag for tag in words if tag.startswith("filter")]
            words = [tag for tag in words if not tag.startswith("filter")]

            extract: List[str] = [tag for tag in words if tag.startswith("extract")]
            words = [tag for tag in words if not tag.startswith("extract")]


            ext = os.path.splitext(path)[1][1:]
            if len(words) > 0:
                ext = words[0]
            if len(fenced) == 1:
                parts = fenced[0].split("=")
                if len(parts) == 2:
                    ext = parts[1]


            new_content += content[last:match.start()] # inserindo texto entre matches
            last = match.end()
            new_content += "[](load)[](" + path + ")[](" + tags + ")\n"

            # se não for run, deve limpar o conteúdo não inserindo os arquivos
            if action == Action.RUN:
                if len(fenced) > 0:
                    new_content += "\n```" + ext + "\n"
                if os.path.isfile(path):
                    if len(filter) > 0:
                        output = subprocess.run(["filter", path], stdout=subprocess.PIPE)
                        data = output.stdout.decode("utf-8")
                        new_content += data
                        if data[-1] != "\n":
                            new_content += "\n"
                    elif len(extract) > 0:
                        tag = extract[0].split("=")[1]
                        data = Load.extract_between_tags(open(path).read(), tag)
                        new_content += data
                        if len(data) == 0 or data[-1] != "\n":
                            new_content += "\n"
                    else:
                        data = open(path).read()
                        new_content += open(path).read()
                        if data[-1] != "\n":
                            new_content += "\n"
                else:
                    print("warning: file", path, "not found")
                if fenced:
                    new_content += "```\n\n"
            new_content += "[](load)"
        
        new_content += content[last:]
        return new_content


            

class Save:
    @staticmethod
    # execute filename and content
    def execute(file_content):
        regex = r"\[\]\(save\)\[\]\((.*?)\)\n```[a-z]*\n(.*?)```\n\[\]\(save\)"
        matches = re.finditer(regex, file_content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            path = match.group(1)
            content = match.group(2)
            exists = os.path.isfile(path)
            if exists:
                content_old = open(path).read()
            if not exists or content != content_old:
                with open(path, "w") as f:
                    print("file", path, "updated")
                    f.write(content)

class Main:
    @staticmethod
    def fix_path(target):
        target = os.path.normpath(target)
        if os.path.isdir(target):
            target = os.path.join(target, "Readme.md")
        pieces = target.split(os.sep)
        folder = "."
        if len(pieces) > 1:
            folder = os.sep.join(pieces[:-1])
        return target, folder

    @staticmethod
    def open_file(path): 
        if os.path.isfile(path):
            with open(path) as f:
                file_content = f.read()
                return True, file_content
        print("Warning: File", path, "not found")
        return False, "" 
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('targets', metavar='T', type=str, nargs='*', help='Readmes or folders')
    parser.add_argument('--quiet', '-q', action="store_true", help='quiet mode')
    parser.add_argument('--clean', '-c', action="store_true", help='clean mode')
    args = parser.parse_args()

    if len(args.targets) == 0:
        args.targets.append(".")
    
    action = Action.RUN if not args.clean else Action.CLEAN

    for target in args.targets:
        path, folder = Main.fix_path(target)
        result, original = Main.open_file(path)
        if not result:
            continue
        updated = original
        updated_toc = Toc.execute(updated, action)
        if updated != updated_toc:
            print("toc updated:", target)
            updated = updated_toc
        updated = Load.execute(updated, action)
        Save.execute(updated)
        
        if updated != original:
            with open(path, "w") as f:
                f.write(updated)
                print("mdpp updading", path)

if __name__ == '__main__':
    main()
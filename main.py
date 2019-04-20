# -*- coding: utf-8 -*-

from wox import Wox

from pathlib import Path

import subprocess

CloudStudioDir = Path(r'C:\Users\14049\WordAndStudy\Projects\CloudStudio')
NoteDir = CloudStudioDir / 'Notes'


class NOTE(Wox):

    def query(self, query):
        keys = query.split()
        resultSet = set()
        results = []

        for i, key in enumerate(keys):
            if i == 0:
                resultSet.update(NoteDir.glob('*' + key + '*'))
            else:
                tmpSet = set(NoteDir.glob('*' + key + '*'))
                resultSet &= tmpSet
        if len(resultSet) > 0:
            for result in resultSet:
                results.append({
                    "Title": result.name,
                    "SubTitle": str(result),
                    "IcoPath": "Images\\icons8_note_25px.png",
                    "ContextData": "ctxData",
                    "JsonRPCAction": {
                        #You can invoke both your python functions and Wox public APIs .
                        #If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                        #you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                        #just replace xxx with the name provided in this url
                        "method": "openFile",
                        #you MUST pass parater as array
                        "parameters": [str(result)],
                        #hide the query wox or not
                        "dontHideAfterAction": True
                    }
                })
        else:
            results.append({
                "Title": "no such note...",
                "SubTitle": "open and create it",
                "IcoPath": "Images\\icons8_note_25px.png",
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    #You can invoke both your python functions and Wox public APIs .
                    #If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                    #you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                    #just replace xxx with the name provided in this url
                    "method": "openFile",
                    #you MUST pass parater as array
                    "parameters": [str(NoteDir)],
                    #hide the query wox or not
                    "dontHideAfterAction": True
                }
            })
        return results

    def openFile(self, data):
        subprocess.run(['subl', data])


if __name__ == "__main__":
    NOTE()
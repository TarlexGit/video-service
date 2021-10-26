# back

## Project setup
```
poetry install
```

### Compiles and hot-reloads for development

`config for .vscode/launch.json`


```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "program": "${workspaceRoot}/video_service/back/main.py",
            "console": "integratedTerminal"
        },
    ]
}
```

Run `main.py` ("Python: File") or start debugger (Python: FastAPI)
def upload(fileup):
    # funcao responsavel pelo upload do arquivo de log para o servidor
    global urlUpload

    if os.path.exists(fileup):
        files = {'file': open(fileup, 'rb')}
    requests.post(urlUpload, files=files)

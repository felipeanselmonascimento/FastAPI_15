import uvicorn

if __name__ == "__main__":
    #  garante que o servidor só sobe quando você rodar o arquivo diretamente, não quando ele for importado.

    uvicorn.run(
        "src.main.server.server:app",
        # O :app depois do caminho diz qual variável dentro do arquivo é o app FastAPI
        host="0.0.0.0",
        port=3001,
        reload=True
    )




# Cliente → Uvicorn → FastAPI → sua função → resposta

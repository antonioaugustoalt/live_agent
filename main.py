import asyncio
from agent import job_agent

async def run():
    print("🤖 JobAgent online!")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break

        try:
            response = await job_agent.run(user_input)

            # alguns frameworks retornam objeto
            if hasattr(response, "output"):
                print("\nJobAgent:", response.output, "\n")
            else:
                print("\nJobAgent:", response, "\n")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(run())
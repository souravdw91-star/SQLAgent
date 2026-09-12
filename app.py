import sys
from src.agent.builder import build_sql_agent

def main():
    try:
        agent = build_sql_agent()
    except Exception as e:
        print(f"Initialization error: {e}")
        sys.exit(1)

    print("=" * 60)
    print("MySQL Gemini Agent Ready (LangSmith Tracing Enabled)")
    print("Type 'exit' or 'quit' to stop.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nEnter your query: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break

            response = agent.invoke({"input": user_input})
            print("\n--- Answer ---")
            print(response.get("output", "No response generated."))

        except KeyboardInterrupt:
            print("\nAborted by user.")
            break
        except Exception as e:
            print(f"\nExecution error: {e}")

if __name__ == "__main__":
    main()
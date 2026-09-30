import os
from dotenv import load_dotenv, find_dotenv
from langchain_aws import ChatBedrock

# Load environment variables
_ = load_dotenv(find_dotenv())


def test_bedrock_connection():
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_DEFAULT_REGION")

    print(f"Checking credentials...")
    print(f"AWS_ACCESS_KEY_ID present: {bool(aws_access_key)}")
    print(f"AWS_SECRET_ACCESS_KEY present: {bool(aws_secret_key)}")
    print(f"AWS_DEFAULT_REGION: {aws_region}")

    if not all([aws_access_key, aws_secret_key, aws_region]):
        print("\nERROR: Missing AWS credentials in .env file.")
        print(
            "Please update f:/Cursos_code/langchain_course/.env with your actual verification keys."
        )
        return

    print("\nAttempting to initialize ChatBedrock...")
    try:
        # Using Amazon Nova Lite model
        llm = ChatBedrock(
            model_id="amazon.nova-lite-v1:0",
            model_kwargs=dict(temperature=0),
        )
        response = llm.invoke("Hello, are you working?")
        print("\nSuccess! Response from Bedrock:")
        print(response.content)
    except Exception as e:
        print("\nFailed to invoke model:")
        print(e)
        print("\nCommon issues:")
        print("1. Credentials are invalid.")
        print("2. The specified model is not enabled in your AWS Bedrock console.")
        print("3. Wrong region selected.")


if __name__ == "__main__":
    test_bedrock_connection()

import json
import os

nb_path = r"f:\Cursos_code\langchain_course\lca-langchainV1-essentials\python\L1_fast_agent.ipynb"

def update_notebook():
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # The new robust source code
    new_source = [
        "import os\n",
        "import boto3\n",
        "from botocore.config import Config\n",
        "from langchain_aws import ChatBedrock\n",
        "from langchain.agents import create_agent\n",
        "\n",
        "# Configure retries to handle throttling\n",
        "retry_config = Config(\n",
        "    retries={\n",
        "        'max_attempts': 10,\n",
        "        'mode': 'standard'\n",
        "    }\n",
        ")\n",
        "\n",
        "llm = ChatBedrock(\n",
        "    model_id=\"amazon.nova-lite-v1:0\",\n",
        "    model_kwargs=dict(temperature=0),\n",
        "    region_name=os.getenv(\"AWS_DEFAULT_REGION\", \"us-east-1\"),\n",
        "    config=retry_config\n",
        ")\n",
        "\n",
        "agent = create_agent(\n",
        "    model=llm,\n",
        "    tools=[execute_sql],\n",
        "    system_prompt=SYSTEM_PROMPT,\n",
        "    context_schema=RuntimeContext,\n",
        ")"
    ]

    target_found = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            source_text = "".join(cell["source"])
            # Target the cell we previously modified or the original if it wasn't
            if ('ChatBedrock' in source_text and 'amazon.nova-lite-v1:0' in source_text) or \
               ('create_agent' in source_text and 'model="openai' in source_text):
                print("Found target cell. Updating with retry config...")
                cell["source"] = new_source
                target_found = True
                # We assume only one such cell needs this specific initialization in L1
                break
    
    if target_found:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("Notebook updated successfully.")
    else:
        print("Target cell not found.")

if __name__ == "__main__":
    update_notebook()

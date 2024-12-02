import tempfile
import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor


OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
llm_config = {"model": "gpt-4", "api_key": OPENAI_API_KEY}
llm_config_crazy = {"model": "gpt-3.5-turbo", "temperature": 1.2, "api_key": OPENAI_API_KEY}
llm_config_json = {"model": "gpt-3.5-turbo-1106", "api_key": OPENAI_API_KEY, "response_format": { "type": "json_object" }}

# ユーザー
human_proxy = ConversableAgent(
    "User1",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)


designer_agent1 = ConversableAgent(
    "Designer1",
    system_message="あなたはソフトウェアの設計者です。ソフトウェアに盛り込む機能を提案してください。言語は日本語を話してください。",
    llm_config=False,
    human_input_mode="NEVER",  # Never ask for human input.
)

designer_agent1_1 = ConversableAgent(
    "Designer1_1",
    system_message="あなたはソフトウェアの設計者です。ソフトウェアに盛り込む機能を提案してください。言語は日本語を話してください。",
    llm_config={"config_list": [llm_config]},
    human_input_mode="NEVER",  # Never ask for human input.
)

crazy_agent = ConversableAgent(
    "Crazy1",
    system_message="あなたはアイデアマンです。とにかく誰も想像していないような突発的なアイデアを提案してください。言語は日本語で話してください。",
    llm_config={"config_list": [llm_config_crazy]},
    human_input_mode="NEVER",  # Never ask for human input.
)

nested_chats = [
    {
        "recipient": designer_agent1_1,
        "summary_method": "reflection_with_llm",
        "max_turns": 1,
    },
    {
        "recipient": crazy_agent,
        "message": "想像力を働かせて色々なアイデアを生成してください。",
        "summary_method": "reflection_with_llm",
        "max_turns": 1,
    },
    {
        "recipient": designer_agent1_1,
        "message": "前者の意見を踏まえて、自分の意見を生成してください。",
        "max_turns": 1,
        "summary_method": "last_msg",
    },
]

designer_agent1.register_nested_chats(
    nested_chats,
    # The trigger function is used to determine if the agent should start the nested chat
    # given the sender agent.
    # In this case, the arithmetic agent will not start the nested chats if the sender is
    # from the nested chats' recipient to avoid recursive calls.
     trigger=lambda sender: sender not in [crazy_agent, designer_agent1_1],
)

designer_agent2 = ConversableAgent(
    "Designer2",
    system_message="あなたはソフトウェアの設計者です。ソフトウェアの妥当性について検討してください。言語は日本語を話してください。",
    llm_config={"config_list": [llm_config]},
    human_input_mode="NEVER",  # Never ask for human input.
)



programmer = ConversableAgent(
    "Programmer1",
    system_message="あなたはアプリケーションのプログラマーです。コードの生成を行ってください。言語は日本語を話してください。",
    llm_config={"config_list": [llm_config]},
    human_input_mode="NEVER",  # Never ask for human input.
)


project = ConversableAgent(
    "project1",
    system_message="あなたはチャットのファシリテータです。背景を日本語で要約してください。",
    llm_config={"config_list": [llm_config]}, # Turn off LLM for this agent.
    human_input_mode="NEVER",  # Always take human input for this agent for safety.
)

json_maker = ConversableAgent(
    "json_maker1",
    llm_config={"config_list": [llm_config_json]}, # Turn off LLM for this agent.
    human_input_mode="NEVER",  # Always take human input for this agent for safety.
)
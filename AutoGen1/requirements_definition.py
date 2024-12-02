import AutoGen1.agent as agent
import subprocess
import json
from autogen import GroupChat
from autogen import GroupChatManager


class Requirements_Definition:

    def __init__(self, task_input: str = None):

        self.task_input = task_input
        





    def conversation(self):
        # グループチャットを作成する。
        group_chat_design = GroupChat(
            agents=[agent.human_proxy, agent.designer_agent1, agent.designer_agent2],
            messages=["グループチャットを終了した際のまとめについては、ソフトウェアの大まかな説明を最初に施し、その後に、実装する機能を細かく説明してください。常に日本語を用いてください。"],
        )
        
        
        # グループチャットマネージャーを作成する。
        group_chat_design_manager = GroupChatManager(
            groupchat=group_chat_design,
            llm_config={"config_list": [agent.llm_config]},
            # system_message="グループチャットを終了した際のまとめについては、ソフトウェアの大まかな説明を最初に施し、その後に、実装する機能を細かく説明してください。",
            is_termination_msg=lambda msg: "これで会議を終わります" in msg["content"].lower(),
        )
        
        chat_result = agent.project.initiate_chats(
            [
                {
                    "recipient": group_chat_design_manager,
                    "message": "今からソフトウェア開発における要件定義を始めます。User1の要望:{}".format(self.task_input),
                    "max_turns": 1,
                    "summary_method": "reflection_with_llm",
                },
                {
                    "recipient": agent.json_maker,
                    "message":  """まとめられた要件定義の内容から、プロジェクト名をname、プロジェクトの内容をtaskというキーとしてjson形式で出力してください。""",
                    "max_turns": 1,
                    "summary_method": "last_msg",
                },
            ]
        )
        project_str = chat_result[-1].summary
        
        with open("project.json", "w", encoding="utf-8") as file:
            file.write(project_str)
        
        with open("project.json", 'r', encoding="utf8") as file:
            project = json.load(file)
        
        name = project["name"]
        task = project["task"]
    
        return name, task
    
        
        
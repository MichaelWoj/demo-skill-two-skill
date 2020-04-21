from mycroft import MycroftSkill, intent_file_handler


class DemoSkillTwo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('two.skill.demo.intent')
    def handle_two_skill_demo(self, message):
        self.speak_dialog('two.skill.demo')


def create_skill():
    return DemoSkillTwo()


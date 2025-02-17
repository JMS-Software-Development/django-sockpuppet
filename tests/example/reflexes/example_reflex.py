from sockpuppet.reflex import Reflex


class ExampleReflex(Reflex):
    def increment(self, step=1):
        self.session['count'] = int(self.element.dataset['count']) + step


class DecrementReflex(Reflex):
    def decrement(self, step=1):
        self.session['otherCount'] = int(self.element.dataset['count']) - step


class ParamReflex(Reflex):
    def change_word(self):
        self.word = 'space'
        self.success = True


class FormReflex(Reflex):
    def submit(self):
        self.text_output = self.request.POST['text-input']


class ErrorReflex(Reflex):
    def increment(self, step=1):
        raise Exception('error happened')


class UserReflex(Reflex):
    def get_user(self):
        context = self.get_context_data()
        self.user_reveal = context['object']


class MorphReflex(Reflex):
    def morph_me(self):
        self.morph('#morph', 'I got morphed!')

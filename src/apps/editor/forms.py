from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django import forms

from taggit.forms import TagWidget
from src.apps.core.forms import *

from polymorphic.formsets import (
        polymorphic_inlineformset_factory,
        BasePolymorphicInlineFormSet,
        PolymorphicFormSetChild
    )

from django.utils.translation import gettext as _

from src.apps.core.models.QuizQuestionModels import (
    QuizQuestion,
    QuizAnswer,

)

from src.apps.core.models.HS_AppFrameModels import (
    AppReference,
)

from src.apps.uploads.models import (
    Image,
)

''' **********************************************************
    Model Forms 
********************************************************** '''

class editor_LessonForm(CreationTrackingForm):
    # content = forms.CharField(
    #         label='Content',
    #         widget=TextEditorWidget(placeholder=True),
    #         # widget=TextEditorWidget(placeholder=True, configuration=cms_settings.CMS_PLACEHOLDER_CONF['lesson_summary']),
    #         required=False,
    #         help_text=_("Optional. If provided, this text will be added to the lesson."),
    #     )
    #name = forms.CharField(min_length=4)

    # internal field marking if form was submitted for deletion
    # delete_on_submit = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)

    class Meta:
        model = Lesson
        fields = [
            'name',
            'short_name',
            'tags',
            'position',
            'summary',


        ]

        widgets = {
            'position': forms.HiddenInput(),

            'name': forms.TextInput(
                    attrs={
                        'required': 'true',
                        'class':'object_name'
                    },
                ),

            'tags': TagWidget(attrs={
                    'class': 'tag_input',
                    'data-role': "tagsinput",
                    'placeholder': 'Add Tags',
                }),

            'summary': forms.HiddenInput(),
        }

    def clean_name(self):

        # add a validation check for the name to be minimum 4 characters
        name = self.cleaned_data.get('name', '')
        if len(name) < 4:
            raise ValidationError("Lesson name must be at least 4 characters.")

        return name

class editor_SectionForm(CreationTrackingForm):
    #content = forms.CharField(widget=TextEditorWidget)
    # name = forms.CharField(min_length=4)
    class Meta:
        model = Section
        fields = [
            'name',
            'short_name',
            'duration',
            'tags',
            'position',
        ]

        widgets = {
            'position': forms.HiddenInput(),
            'name': forms.TextInput(
                    attrs={
                            'required': 'true',
                            'class': 'object_name'
                        },
                    ),
            'tags': TagWidget(attrs={
                    'class': 'tag_input',
                    'data-role': "tagsinput",
                    'placeholder': 'Add Tags',

                }),

        }

    def clean_name(self):

        # add a validation check for the name to be minimum 4 characters
        name = self.cleaned_data.get('name', '')
        if len(name) < 4:
            raise ValidationError("Section name must be at least 4 characters.")

        return name

class editor_AppRefForm(forms.ModelForm):
    class Meta:
        model = AppReference
        fields = [
            'app_name',
            'app_link',
        ]

#
# # generic content form for use by Lessons/Sections
# # to store CKEditor
# class editor_ContentForm(forms.Form):
#     # the CKEditor Content
#     content = forms.TextInput()
#
#     # the Model Type associated with the content
#     model_type = forms.CharField(widget=forms.HiddenInput())
#
#     # collection of included images in the content
#     #       need a way to handle images in content and
#     #       mark Image.is_temp = False on save
#     #       and store a mapping between that image and the content model
#     images = forms.ModelMultipleChoiceField(queryset=Image.objects.none(), widget=forms.HiddenInput())
#
#
#     class Media:
#         # include the custom CK5 Build in this form
#         js = [
#             '/static/editor/js/HL_ck5_custom.js',
#         ]



''' **********************************************************
POLYMORPHIC FORM TYPES
********************************************************** '''

class editor_ReadingSectionForm(CreationTrackingForm):
    class Meta:
        model = ReadingSection
        fields = [
            'name',
            'short_name',
            'duration',
            'tags',
            'position',
            'content',

        ]
        widgets = {
            'position': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                    'required': 'true',
                    'class':'object_name'
                }),
            'tags': TagWidget(attrs={
                    'class': 'tag_input',
                    'data-role': "tagsinput",
                    'placeholder': 'Add Tags',

                }),
            'content': forms.HiddenInput(),


        }



class editor_ActivitySectionForm(CreationTrackingForm):
    class Meta:
        model = ActivitySection
        fields = [
            'name',
            'short_name',
            'duration',
            'tags',
            'position',
            'content',
        ]

        widgets = {
            # 'content': TextEditorWidget(),
            'position': forms.HiddenInput(),
            #'topic': apply_select2(forms.Select),
            'name': forms.TextInput(attrs={
                    'required': 'true',
                    'class':'object_name'
                }),
            'tags': TagWidget(attrs={
                    'class': 'tag_input',
                    'data-role': "tagsinput",
                    'placeholder': 'Add Tags',


                }),
            'content': forms.HiddenInput(),

        }

        readonly_fields = ['topic']
        # exclude = ['created_by']



class editor_QuizSectionForm(CreationTrackingForm):
    class Meta:
        model = QuizSection
        fields = [
            'name',
            'short_name',
            'duration',
            'tags',
            'position',
        ]

        widgets = {
            # 'content': TextEditorWidget(),
            'position': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                    'required': 'true',
                    'class': 'object_name'
                }),
            #'duration':
            #'topic': apply_select2(forms.Select),
            'tags': TagWidget(attrs={
                    'class': 'tag_input',
                    'data-role': "tagsinput",
                    'placeholder': 'Add Tags',

                }),
        }

        readonly_fields = ['topic']
        # exclude = ['created_by']




''' **********************************************************
    Quiz Question/answer Forms
********************************************************** '''

class editor_QuizQuestionForm(forms.ModelForm):
    #question_text = forms.Textarea(attrs={'class':'question_text_input'})
    class Meta:
        model = QuizQuestion
        fields = [
            'question_type',
            'question_text',

            'position',
        ]

        widgets = {
            # 'content': TextEditorWidget(),
            'position': forms.HiddenInput(),

            'question_text': forms.Textarea(attrs={
                'class':'question_text_input',
                'cols': '75',
                'rows': '3',
                #'required': True,
            }),
        }


class editor_AnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer

        fields = [
            'is_correct',
            'answer_text',
            'position',
        ]

        widgets = {
            # 'content': TextEditorWidget(),
            'position': forms.HiddenInput(),

            'answer_text': forms.Textarea(attrs={
                'class': 'answer_text_input',
                'cols': '75',
                'rows': '3',
                #'required': True,
            }),
        }


''' **********************************************************
    Inline Formsets
********************************************************** '''

class BaseLessonFormset(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseLessonFormset, self).__init__(*args, **kwargs)

        #self.prefix = "TOPIC"
        for form in self.forms:
            form.empty_permitted = False

    def add_fields(self, form, index):
        super(BaseLessonFormset, self).add_fields(form, index)

        if self.can_delete:
            form.fields['DELETE'] = forms.BooleanField(
                label=_('Delete'),
                required=False,
                widget=forms.HiddenInput
            )

        # add the inline formset for sub_lessons in each lesson
        form.sub_lessons = inlineLessonFormset(
                instance=form.instance,
                data=form.data if self.is_bound else None,
                # data=form.data if form.is_bound else None,
                # files=form.files if form.is_bound else None,
                prefix='%s-%s' % (
                    form.prefix,
                    inlineLessonFormset.get_default_prefix()
                ),
            )

        #add the inline formset for child_sections in each topic
        form.child_sections = inlineSectionFormset(
                    instance=form.instance,
                    data=form.data if self.is_bound else None,
                    #data=form.data if form.is_bound else None,
                    #files=form.files if form.is_bound else None,
                    prefix='%s-%s' % (
                        form.prefix,
                        inlineSectionFormset.get_default_prefix()
                    ),
                )

    def is_valid(self):
        result = super(BaseLessonFormset, self).is_valid()

        if(self.is_bound):
            # look at any nested formsets as well
            for form in self.forms:
                result = result and form.sub_lessons.is_valid()
                result = result and form.child_sections.is_valid()


        return result

    def clean(self):

        # if any forms already have errors return
        if any(self.errors):
            return

        #   check that each topic name is unique
        encountered_name = []
        for lesson in self.forms:
            if self.can_delete:
                if self._should_delete_form(lesson):
                    # This form is going to be deleted so any of its errors
                    # should not cause the entire formset to be invalid.
                    continue


            curr_name = lesson.cleaned_data.get('name')
            #marked_delete = lesson.cleaned_data.get('DELETE')

            if curr_name in encountered_name:
                lesson.add_error("name","Each Lesson name must be unique within it's parent.")

            #if not marked_delete:
            encountered_name.append(curr_name)




            # for section in lesson.child_sections:
            #     section.clean()

        # perform the standard clean
        super(BaseLessonFormset, self).clean()

    def save(self, commit=True):
        # get the result of saving the base topics
        result = super(BaseLessonFormset, self).save(commit=commit)

        # POTENTIALLY NEED TO ITERATE OVER 'result' NOT SELF.FORMS

        # for each form in this formset
        if commit:
            for form in self.forms:
                # save child sections if form isn't marked for deletion
                if not self._should_delete_form(form):
                    form.sub_lessons.save(commit=commit)
                    form.child_sections.save(commit=commit)

        return result

class BaseSectionFormset(BasePolymorphicInlineFormSet):

    # def __init__(self, *args, **kwargs):
    #     super(BaseSectionFormset, self).__init__(*args, **kwargs)
    #     self.prefix = "SECTION"

    def add_fields(self, form, index):
        super(BaseSectionFormset, self).add_fields(form, index)


        if self.can_delete:
            form.fields['DELETE'] = forms.BooleanField(
                label=_('Delete'),
                required=False,
                widget=forms.HiddenInput
            )

    def save(self, commit=True):
        # get the result of saving the base topics
        result = super(BaseSectionFormset, self).save(commit=commit)

        #
        # # if actually committing save it's many to many relationships (tags)
        # if commit:
        #     for form in self.forms:
        #         form.save_m2m()

        return result

    def clean(self):

        # if any forms already have errors return
        if any(self.errors):
            return

        #  Check that each section name is unique
        encountered_name = []
        for section in self.forms:
            if self.can_delete:
                if self._should_delete_form(section):
                    # This form is going to be deleted so any of its errors
                    # should not cause the entire formset to be invalid.
                    continue

            curr_name = section.cleaned_data['name']
            #marked_delete = section.cleaned_data.get('DELETE')

            if curr_name in encountered_name:
                #raise forms.ValidationError("Each Section Name must be unique within a Topic!")
                section.add_error('name', "Each Section Name must be unique within a Lesson!")

            #if not marked_delete:
            encountered_name.append(curr_name)

        # perform the standard clean
        super(BaseSectionFormset, self).clean()

class BaseQuizQuestionFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseQuizQuestionFormset, self).add_fields(form, index)


        if self.can_delete:
            form.fields['DELETE'] = forms.BooleanField(
                label=_('Delete'),
                required=False,
                widget=forms.HiddenInput
            )

            # add the inline formset for sub_lessons in each lesson
            form.answers = inlineQuizAnswerFormset(
                instance=form.instance,
                data=form.data if self.is_bound else None,
                prefix='%s-%s' % (
                    form.prefix,
                    inlineQuizAnswerFormset.get_default_prefix()
                ),
            )

    def is_valid(self):
        result = super(BaseQuizQuestionFormset, self).is_valid()

        if(self.is_bound):
            # look at any nested formsets as well
            for form in self.forms:
                valid_answers = form.answers.is_valid()

                if not valid_answers:
                    form.add_error(None, form.answers.errors)
                    form.add_error(None, form.answers.non_form_errors())



                result = result and valid_answers

        return result

class BaseQuizAnswerFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseQuizAnswerFormset, self).add_fields(form, index)


        if self.can_delete:
            form.fields['DELETE'] = forms.BooleanField(
                label=_('Delete'),
                required=False,
                widget=forms.HiddenInput
            )

    def clean(self):
        if any(self.errors):
            return

        num_populated = sum(a.cleaned_data.get('answer_text', '') != '' for a in self.forms)
        num_correct = sum(a.cleaned_data.get('answer_text', '') != '' and a.cleaned_data.get('is_correct', False) for a in self.forms)

        if num_populated < 2:
            result = False
            # self.add_error(None, 'You Must Provide at least TWO possible answers for quiz question.')
            raise forms.ValidationError('You Must Provide at least TWO possible answers for quiz question.')

        if num_correct == 0:
            result = False
            raise forms.ValidationError('At least one answer must be correct in each quiz question.')

    def is_valid(self):
        result = super(BaseQuizAnswerFormset, self).is_valid()

        if not self.is_bound:
            return False

        result = True

        # the answer formset is valid if it has at least 2 answers
        #   and at least one entry is marked as correct
        num_populated = sum(a.cleaned_data.get('answer_text', '') != '' for a in self.forms)
        num_correct = sum(a.cleaned_data.get('answer_text', '') != '' and a.cleaned_data.get('is_correct', False) for a in self.forms)

        if num_populated < 2:
            result = False

        if num_correct == 0:
            result = False

        return result

''' **********************************************************
Formset Factories
********************************************************** '''

inlineLessonFormset = inlineformset_factory(
        Lesson,
        Lesson,
        fk_name='parent_lesson', #need to specify the field linking to parent lesson
        exclude=['published_copy','created_by', 'changed_by','creation_date', 'changed_date'],
        extra=0,
        form=editor_LessonForm,
        formset=BaseLessonFormset,

    )

#SectionFormset = inlineformset_factory(Topic, Section, formset=BaseSectionFormset, extra=1)
inlineSectionFormset = polymorphic_inlineformset_factory(
    Lesson,
    Section,
    exclude=['created_by', 'changed_by','creation_date', 'changed_date'],
    extra=0,
    formset=BaseSectionFormset,
    formset_children=( # add the inline polymorphic children and link their custom forms.
            PolymorphicFormSetChild(ReadingSection, editor_ReadingSectionForm),
            PolymorphicFormSetChild(QuizSection, editor_QuizSectionForm),
            PolymorphicFormSetChild(ActivitySection, editor_ActivitySectionForm),

        )
    )

inlineQuizQuestionFormset = inlineformset_factory(
    QuizSection,
    QuizQuestion,
    extra=1,
    #fields=['question_type', 'question_text'],
    form=editor_QuizQuestionForm,
    formset=BaseQuizQuestionFormset,

)

inlineQuizAnswerFormset = inlineformset_factory(
    QuizQuestion,
    QuizAnswer,
    #fields=['answer_text'],
    form=editor_AnswerForm,
    formset=BaseQuizAnswerFormset,
    extra=4,
    max_num=4,
    min_num=2,
)

inlineLearning_ObjectiveFormset = inlineformset_factory(
    Lesson,
    Learning_Objective,
    form=Learning_ObjectiveTextForm,
    extra=1,
    can_delete=True,
)


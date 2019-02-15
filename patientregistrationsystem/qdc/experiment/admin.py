from django.contrib import admin
from import_export import resources
from simple_history.admin import SimpleHistoryAdmin
from modeltranslation.admin import TranslationAdmin

from .models import QuestionnaireResponse, StimulusType, Tag, ADConverter, StandardizationSystem, ElectrodeShape, \
    MeasureSystem, MeasureUnit, TetheringSystem, AmplifierDetectionType, ElectrodeConfiguration, CoilOrientation, \
    DirectionOfTheInducedCurrent, BrainArea, BrainAreaSystem, InformationType, GoalkeeperGame, GoalkeeperPhase, \
    ResearchProject, Experiment, Group, Component, ComponentConfiguration, ComponentAdditionalFile

admin.site.register(QuestionnaireResponse, SimpleHistoryAdmin)


class StimulusTypeAdmin(TranslationAdmin):
    pass


admin.site.register(StimulusType, StimulusTypeAdmin)
admin.site.register(Tag)

admin.site.register(ElectrodeShape)
admin.site.register(MeasureSystem)
admin.site.register(MeasureUnit)
admin.site.register(TetheringSystem)
admin.site.register(AmplifierDetectionType)
admin.site.register(ElectrodeConfiguration)
admin.site.register(ADConverter)
admin.site.register(StandardizationSystem)
admin.site.register(CoilOrientation)
admin.site.register(DirectionOfTheInducedCurrent)
admin.site.register(BrainArea)
admin.site.register(BrainAreaSystem)
admin.site.register(InformationType)
admin.site.register(GoalkeeperGame)
admin.site.register(GoalkeeperPhase)


class ResearchProjectResource(resources.ModelResource):

    class Meta:
        model = ResearchProject
        exclude = ('id', 'owner')

    def export(self, queryset=None, *args, **kwargs):
        queryset = ResearchProject.objects.filter(id=kwargs['id'])
        return super(ResearchProjectResource, self).export(queryset, *args, **kwargs)

    def get_instance(self, instance_loader, row):
        return False


class ExperimentResource(resources.ModelResource):

    class Meta:
        model = Experiment
        exclude = ('id', 'last_update', 'last_sending')

    def export(self, queryset=None, *args, **kwargs):
        queryset = Experiment.objects.filter(id=kwargs['id'])
        return super(ExperimentResource, self).export(queryset, *args, **kwargs)

    def get_instance(self, instance_loader, row):
        return False


class GroupResource(resources.ModelResource):

    class Meta:
        model = Group
        exclude = ('experiment', 'id')

    def export(self, queryset=None, *args, **kwargs):
        queryset = Group.objects.filter(experiment=kwargs['experiment'])
        return super(GroupResource, self).export(queryset, *args, **kwargs)

    def get_instance(self, instance_loader, row):
        return False


class ComponentResource(resources.ModelResource):

    class Meta:
        model = Component

    def export(self, queryset=None, *args, **kwargs):
        queryset = Component.objects.filter(id__in=kwargs['ids'])
        return super(ComponentResource, self).export(queryset, *args, **kwargs)

    def get_instance(self, instance_loader, row):
        return False


class ComponentConfigResource(resources.ModelResource):

    class Meta:
        model = ComponentConfiguration
        exclude = ('id', )

    def export(self, queryset=None, *args, **kwargs):
        queryset = ComponentConfiguration.objects.filter(parent_id__in=kwargs['ids'])
        return super(ComponentConfigResource, self).export(queryset, *args, **kwargs)

    def get_instance(self, instance_loader, row):
        return False

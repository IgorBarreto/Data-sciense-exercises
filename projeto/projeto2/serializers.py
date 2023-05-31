from rest_framework import serializers
from projeto2.models import CancerMama


class CancerMamaSerializerUploadFile(serializers.Serializer):
    file = serializers.FileField()


class CancerMamaSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = CancerMama
        fields = [
            'id',
            'idade',
            'menopausa',
            'inv_nodes',
            'deg_malig',
            'classe_binarizada',
            'irradiando_binarizada',
            'node_caps_binarizada',
            'seio_binarizada',
            'tamanho_tumor_binarizada',
            'quadrante_binarizada',
            'menopausa_lable_encoding',
            'posicao_tumor_concatenate',
            'deg_malig_1',
            'deg_malig_2',
            'deg_malig_3',
        ]

    classe_binarizada = serializers.SerializerMethodField()
    irradiando_binarizada = serializers.SerializerMethodField()
    node_caps_binarizada = serializers.SerializerMethodField()
    seio_binarizada = serializers.SerializerMethodField()
    tamanho_tumor_binarizada = serializers.SerializerMethodField()
    quadrante_binarizada = serializers.SerializerMethodField()
    posicao_tumor_concatenate = serializers.SerializerMethodField()
    deg_malig_1 = serializers.SerializerMethodField()
    deg_malig_2 = serializers.SerializerMethodField()
    deg_malig_3 = serializers.SerializerMethodField()
    menopausa_lable_encoding = serializers.SerializerMethodField()

    def get_deg_malig_1(self, obj):
        if obj.deg_malig == 1:
            return 1
        return 0

    def get_deg_malig_2(self, obj):
        if obj.deg_malig == 2:
            return 1
        return 0

    def get_deg_malig_3(self, obj):
        if obj.deg_malig == 3:
            return 1
        return 0

    def get_posicao_tumor_concatenate(self, obj):
        return f'{obj.inv_nodes} {obj.quadrante}'

    def get_menopausa_lable_encoding(self, obj):
        print(obj)
        if obj.menopausa == 'ge40':
            return 1
        elif obj.menopausa == 'premeno':
            return 2
        elif obj.menopausa == 'lt40':
            return 3

    def get_classe_binarizada(self, obj):
        if obj.classe == 'no-recurrence-events':
            return 0
        elif obj.classe == 'recurrence-events':
            return 1

    def get_irradiando_binarizada(self, obj):
        if obj.irradiando == 'no':
            return 0
        elif obj.irradiando == 'yes':
            return 1

    def get_node_caps_binarizada(self, obj):
        if obj.node_caps == 'no':
            return 0
        elif obj.node_caps == 'yes':
            return 1
        else:
            return 2

    def get_seio_binarizada(self, obj):
        if obj.seio == 'left':
            return 'E'
        elif obj.seio == 'right':
            return 'D'

    def get_tamanho_tumor_binarizada(self, obj):
        if obj.tamanho_tumor == '0-4' or obj.tamanho_tumor == '5-9':
            return 'Muito Pequeno'
        elif obj.tamanho_tumor == '10-14' or obj.tamanho_tumor == '15-19':
            return 'Pequeno'
        elif obj.tamanho_tumor == '20-24' or obj.tamanho_tumor == '25-29':
            return 'Médio'
        elif obj.tamanho_tumor == '30-34' or obj.tamanho_tumor == '35-39':
            return 'Grande'
        elif obj.tamanho_tumor == '40-44' or obj.tamanho_tumor == '45-49':
            return 'Muito Grande'
        elif obj.tamanho_tumor == '50-54' or obj.tamanho_tumor == '55-59':
            return 'Tratamento Urgente'

    def get_quadrante_binarizada(self, obj):
        if obj.quadrante == 'left_low':
            return 1
        elif obj.quadrante == 'right_up':
            return 2
        elif obj.quadrante == 'left_up':
            return 3
        elif obj.quadrante == 'right_low':
            return 4
        elif obj.quadrante == 'central':
            return 5
        else:
            return 0

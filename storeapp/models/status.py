# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Status(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Descrição",
                                help_text='Descrição.')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=False)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "storeapp"
        verbose_name = 'Satus'
        verbose_name_plural = 'Status'
        permissions = (
            ("store_add_produto", "Adicionar Produto"),
            ("store_detail_produto", "Visualizar Produto"),
        )

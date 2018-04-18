# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from mongoengine import connect
from wtforms import *
from wtforms.validators import DataRequired, Email

from controle.models.models import Processo


class NovoProcessoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = StringField('Descricao', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    salvar = SubmitField('Salvar')


class AdicionarGrupoHostsForm(FlaskForm):
    nome_processo = StringField('Processo', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = StringField('Descricao', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    novo_grupo = StringField('Nome novo grupo', validators=[DataRequired()])
    hosts = TextAreaField(validators=[DataRequired()])

    salvar = SubmitField('Salvar')


class RemoverGrupoHostsForm(FlaskForm):
    nome_processo = StringField('Processo', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = StringField('Descricao', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    grupo_removido = StringField('Nome do grupo a remover', validators=[DataRequired()])
    hosts = TextAreaField(validators=[DataRequired()])

    salvar = SubmitField('Salvar')
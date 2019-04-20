# coding: utf-8

from rest_framework import serializers

from .models import Book, Impression


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page')


class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impression
        fields = ('book', 'comment')

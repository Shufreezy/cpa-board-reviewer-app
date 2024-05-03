import os

from flask import render_template, redirect, request
from ..reviewer.context import context as reviewer_context
from . import google_service

def home():
    home_context = {
        'title': 'Boards Reviewer Application',
        'summaries': google_service.get_learnings()
    }
    return render_template("base.html", **home_context)

def reviewer():
    return render_template("pages/reviewer.html", **reviewer_context)
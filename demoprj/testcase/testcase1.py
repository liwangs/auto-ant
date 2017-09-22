# -*- coding: utf-8 -*-

from knitter import datadriver,log
from demoprj.page import page

def TestCase001_NormalInputTest():
    #### Name ###
    page.Name.Title.Select("Mr.")
    page.Name.Name.Set("Henry.Wang")

    ### Gender ###
    page.Gender.Male.Click()

    ### Hobbies ###
    page.Hobby.Music.Click()
    page.Hobby.Travel.Click()

    ###### Result ######
    page.SubmitButton.Click()

    page.Result.VerifyInnerHTMLContains("Henry.Wang")
    page.Result.VerifyAttribute("innerHTML", "Music", method="contain")

from django.contrib import admin

from django.contrib.admin import register

from portfolio.models import GroupStack, Portfolio, Project, SectionHero, Stack


@register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("section_hero", "active")
    fields = (
        "section_hero",
        "about",
        "groups_stacks",
        "projects",
        "linkedin",
        "github",
        "active",
    )
    filter_horizontal = ("groups_stacks", "projects")


@register(SectionHero)
class SectionHeroAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")
    fields = ("title", "subtitle", "description")


@register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)


@register(GroupStack)
class GroupStackAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", "stacks")
    filter_horizontal = ("stacks",)


@register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    fields = ("title", "slug", "description", "repository")
    prepopulated_fields = {"slug": ("title",)}

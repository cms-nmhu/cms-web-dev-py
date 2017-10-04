from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.widgets import CKEditorWidget


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
	fieldsets = (
		(None, {'fields': ('url', 'title', 'content', 'sites')}),
		(_('Advanced options'), {
			'classes': ('collapse', ),
			'fields': (
				'enable_comments',
				'registration_required',
				'template_name',
			),
		}),
	)

	formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

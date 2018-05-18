from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from whoosh.analysis import *
from whoosh.index import open_dir
from whoosh.fields import *

# Create your models here.
class Entry(models.Model):
    key_ta = models.CharField(_('key (tamil)'), max_length=300)
    key_en = models.CharField(_('key (english)'), max_length=300, blank=True,
    null=True)
    entry = models.TextField(_('entry'))
    
    def __unicode__(self):
        if self.key_en:
            return "%s (%s)" % (self.key_ta, self.key_en)
        else:
            return self.key_ta

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')

    def save(self, **kwargs):
        is_update = False        
        if self.id:
            is_update = True

        super(Entry, self).save(**kwargs)

        ix = open_dir(settings.INDEX_PATH)
        writer = ix.writer()
        if is_update:
            writer.update_document(id = unicode(self.id), key_ta = self.key_ta, key_en = self.key_en, content = self.entry)
        else:
            writer.add_document(id = unicode(self.id), key_ta = self.key_ta, key_en = self.key_en, content = self.entry)
        writer.commit()


    def delete(self):

        if not self.id:
            return
        
        ix = open_dir(settings.INDEX_PATH)
        docs = ix.delete_by_term('id', unicode(str(self.id)))
        ix.commit()
        print "%s docs deleted!" % str(docs)

        ix.commit()

        super(Entry, self).delete()

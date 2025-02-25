# Copyright 2025 Binhex
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade

_xml_ids_renames = [
    ("l10n_es.account_chart_template_common", "l10n_es.es_common"),
    ("l10n_es.account_chart_template_pymes", "l10n_es.es_pymes"),
    ("l10n_es.account_chart_template_assoc", "l10n_es.es_assec"),
    ("l10n_es.account_chart_template_full", "l10n_es.es_full"),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_xmlids(env.cr, _xml_ids_renames)

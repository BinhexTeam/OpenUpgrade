# Copyright 2025 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


def _precreate_fields_computation(env):
    if not openupgrade.column_exists(
        env.cr, "sale_order", "prepayment_percent"
    ):
        openupgrade.add_fields(
            env,
            [
                (
                    "prepayment_percent",
                    "sale.order",
                    "sale_order",
                    "float",
                    False,
                    "sale",
                )
            ],
        )

    if not openupgrade.column_exists(
        env.cr, "sale_order", "amount_to_invoice"
    ):
        openupgrade.add_fields(
            env,
            [
                (
                    "amount_to_invoice",
                    "sale.order",
                    "sale_order",
                    "monetary",
                    False,
                    "sale",
                )
            ],
        )


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.copy_columns(env.cr, {"sale_order": [("state", None, None)]})
    _precreate_fields_computation(env)

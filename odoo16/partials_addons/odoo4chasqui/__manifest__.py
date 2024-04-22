{
    'name': 'Odoo4Chasqui',
    'version': '1.0',
    'summary': 'Módulo para gestionar dependencias para Chasqui',
    'sequence': 10,
    'description': "Este módulo gestiona un conjunto de dependencias necesarias para Chasqui",
    'author': "Chasqui Team Developers",
    'website': "https://tiendaschasqui.ar/",
    'category': 'Sales',
    'license': 'AGPL-3',
    'depends': [
        'base', 'sale', 'purchase', 
        'l10n_ar_afipws', 'l10n_ar_afipws_fe', 'l10n_ar_bank',
        'l10n_ar_account_withholding','l10n_ar_bank','l10n_ar_purchase','l10n_ar_purchase_stock', 'l10n_ar_ux',
        'account_mass_reconcile','account_move_base_import','account_move_line_reconcile_manual','account_move_reconcile_forbid_cancel',,'account_reconcile_oca','account_statement_base','base_transaction_id',
        'account_statement_import_base','account_statement_import_camt','account_statement_import_camt54','account_statement_import_file','account_statement_import_ofx','account_statement_import_online','account_statement_import_online_paypal','account_statement_import_online_ponto','account_statement_import_sheet_file',
        'odoo_chasqui_integration',
        'l10n_ar_report_fe','l10n_ar_fe_qr'
        ], 
    'application': True,
    'installable': True,
    'auto_install': False,
}
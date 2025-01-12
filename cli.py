#!/usr/bin/env python

import click
import logging
import manage

from flask.cli import FlaskGroup
from webservices.common import models
from webservices.rest import app, db
import webservices.legal_docs as legal_docs
from webservices.legal_docs.es_management import DOCS_REPOSITORY_NAME


cli = FlaskGroup(app)
logger = logging.getLogger("cli")


@app.cli.command('load_regulations')
def load_regulations_cli():
    legal_docs.load_regulations()  


@app.cli.command('load_statutes')
def load_statutes_cli():
    legal_docs.load_statutes()


@app.cli.command('load_advisory_opinions')
@click.argument('from_ao_no', default=None, required=False)
def load_advisory_opinions_cli(from_ao_no):
    legal_docs.load_advisory_opinions(from_ao_no)


@app.cli.command('load_current_murs')
@click.argument('specific_mur_no', default=None, required=False)
def load_current_murs_cli(specific_mur_no):
    legal_docs.load_current_murs(specific_mur_no)  


@app.cli.command('load_adrs')
@click.argument('specific_adr_no', default=None, required=False)
def load_adrs_cli(specific_adr_no):
    legal_docs.load_adrs(specific_adr_no)


@app.cli.command('load_admin_fines')
@click.argument('specific_af_no', default=None, required=False)
def load_admin_fines_cli(specific_af_no):
    legal_docs.load_admin_fines(specific_af_no)


@app.cli.command('load_archived_murs')
@click.argument('mur_no', default=None, required=False)
def load_archived_murs_cli(mur_no):
    legal_docs.load_archived_murs(mur_no)


@app.cli.command('extract_pdf_text')
@click.argument('mur_no', default=None, required=False)
def extract_pdf_text_cli(mur_no):
    legal_docs.extract_pdf_text(mur_no)


@app.cli.command('delete_doctype_from_es')
@click.argument('index_name', default=None, required=False)
@click.argument('doc_type', default=None, required=False)
def delete_doctype_from_es_cli(index_name, doc_type):
    legal_docs.delete_doctype_from_es(index_name, doc_type)


@app.cli.command('delete_single_doctype_from_es')
@click.argument('index_name', default=None, required=False)
@click.argument('doc_type', default=None, required=False)
@click.argument('num_doc_id', default=None, required=False)
def delete_single_doctype_from_es_cli(index_name, doc_type, num_doc_id):
    legal_docs.delete_single_doctype_from_es(index_name, doc_type, num_doc_id)


@app.cli.command('delete_murs_from_s3')
def delete_murs_from_s3_cli():
    legal_docs.delete_murs_from_s3()


@app.cli.command('show_legal_data')
def show_legal_data_cli():
    legal_docs.show_legal_data()


@app.cli.command('create_index')
@click.argument('index_name', default=None, required=False)
@click.argument('aliases_name', default=None, required=False)
def create_index_cli(index_name, aliases_name):
    legal_docs.create_index(index_name, aliases_name)  


@app.cli.command('restore_from_staging_index')
def restore_from_staging_index_cli():
    legal_docs.restore_from_staging_index()


@app.cli.command('delete_index')
@click.argument('index_name', default=None, required=False)
def delete_index_cli(index_name):
    legal_docs.delete_index(index_name)


@app.cli.command('display_index_alias')
def display_index_alias_cli():
    legal_docs.display_index_alias()  


@app.cli.command('display_mappings')
def display_mappings_cli():
    legal_docs.display_mappings()


@app.cli.command('initialize_current_legal_docs')
def initialize_current_legal_docs_cli():
    legal_docs.initialize_current_legal_docs()


@app.cli.command('initialize_archived_mur_docs')
def initialize_archived_mur_docs_cli():
    legal_docs.initialize_archived_mur_docs()


@app.cli.command('refresh_current_legal_docs_zero_downtime')
def refresh_current_legal_docs_zero_downtime_cli():
    legal_docs.refresh_current_legal_docs_zero_downtime()


@app.cli.command('configure_snapshot_repository')
@click.argument('index_name', default=DOCS_REPOSITORY_NAME, required=False)
def configure_snapshot_repository_cli(repository_name):
    legal_docs.configure_snapshot_repository(repository_name)


@app.cli.command('delete_repository')
@click.argument('repository_name', default=None, required=False)
def delete_repository_cli(repository_name):
    legal_docs.delete_repository(repository_name)


@app.cli.command('display_repositories')
def display_repositories_cli():
    legal_docs.display_repositories()


@app.cli.command('create_es_snapshot')
@click.argument('repository_name', default=None, required=False)
@click.argument('snapshot_name', default="auto_backup", required=False)
@click.argument('index_name', default=None, required=False)
def create_es_snapshot_cli(repository_name, snapshot_name, index_name):
    legal_docs.create_es_snapshot(repository_name, snapshot_name, index_name)


@app.cli.command('restore_es_snapshot')
@click.argument('repository_name', default=None, required=False)
@click.argument('snapshot_name', default=None, required=False)
@click.argument('index_name', default=None, required=False)
def restore_es_snapshot_cli(repository_name, snapshot_name, index_name):
    legal_docs.restore_es_snapshot(repository_name, snapshot_name, index_name)


@app.cli.command('restore_es_snapshot_downtime')
@click.argument('repository_name', default=None, required=False)
@click.argument('snapshot_name', default=None, required=False)
@click.argument('index_name', default=None, required=False)
def restore_es_snapshot_downtime_cli(repository_name, snapshot_name, index_name):
    legal_docs.restore_es_snapshot_downtime(repository_name, snapshot_name, index_name)


@app.cli.command('delete_snapshot')
@click.argument('repository_name', default=None, required=False)
@click.argument('snapshot_name', default=None, required=False)
def delete_snapshot_cli(repository_name, snapshot_name):
    legal_docs.delete_snapshot(repository_name, snapshot_name)


@app.cli.command('display_snapshots')
@click.argument('repository_name', default=None, required=False)
def display_snapshots_cli(repository_name):
    legal_docs.display_snapshots(repository_name)


@app.cli.command('display_snapshot_detail')
@click.argument('repository_name', default=None, required=False)
@click.argument('snapshot_name', default=None, required=False)
def display_snapshot_detail_cli(repository_name, snapshot_name):
    legal_docs.display_snapshot_detail(repository_name, snapshot_name)


@app.cli.command('refresh_materialized')
@click.argument('concurrent', default=True, type=bool)
def refresh_materialized_cli(concurrent=True):
    manage.refresh_materialized()


@app.cli.command('cf_startup')
def cf_startup_cli():
    manage.cf_startup()


@app.cli.command('slack_message')
@click.argument('message')
def slack_message_cli(message):
    manage.slack_message(message)


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'models': models}


if __name__ == "__main__":
    cli()

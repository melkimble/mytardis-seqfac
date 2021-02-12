mytardis-seqfac
===============
cd /opt/mytardis/develop/tardis/apps
git clone https://github.com/melkimble/mytardis-seqfac sequencing_facility

pip install -r requirements.txt

INSTALLED_APPS += ('tardis.apps.mydata',)

python manage.py loaddata tardis/apps/sequencing_facility/fixtures/sequencing_facility_schema.json
python manage.py loaddata tardis/apps/sequencing_facility/fixtures/instrument.json
python manage.py loaddata tardis/apps/sequencing_facility/fixtures/facility.json
python manage.py loaddata tardis/apps/sequencing_facility/fixtures/trash_user.json



The MyTardis Sequencing Facility app ('`mytardis-seqfac`') is a 
component of the MyTardis data management server which enables 
ingestion, storage, reporting and sharing of high throughput sequencing 
data for genomics projects. 

You can read more about the project here: http://www.mytardis.org/news/mytardis-for-genomics

Dependencies
------------

  * A [MyTardis](https://github.com/mytardis/mytardis) server
  
Python dependencies are installed from requirements.txt

To ingest data, use the [mytardis_ngs_ingestor](https://github.com/mytardis/mytardis_ngs_ingestor) 
client.

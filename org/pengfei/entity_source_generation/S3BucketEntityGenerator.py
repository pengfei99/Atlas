from org.pengfei.entity_source_generation.utile import *
import os

# get current path
base_path = os.getcwd()

config = init_config()


# get s3_bucket attributes list
def get_s3_bucket_all_supported_attributes():
    return {
        'entity_type': "aws_s3_bucket",
        'name': "Required attribute. "
                "The name of the s3 bucket, Example, donnees-insee",
        'domain': "Required attribute. "
                  " The domain of your s3. Example, minio.lab.sspcloud.fr",
        'qualified_name': "Required attribute. "
                          " Fully qualified name of the s3 bucket. It must be unique"
                          " Example, s3://minio.lab.sspcloud.fr/donnees-insee  ",
        'description': "Required attribute. "
                       "The description of the entity",
        'creator_id': "User id of the entity creator",
        'updator_id': "User id of the entity updater",
        'create_time': "Creation time of the entity",
        'update_time': "Last modification time of the entity ",
        'owner': "User id of the entity provider",
        'encryptionType': 'If data is encrypted, we specify the encryption algorithm here',
        'partner': 'none',
        'isEncrypted': "Indicate if data is encrypted or not, only boolean value is accepted. Example, True, False",
        'region': 'none',
    }


def generate_s3_bucket_json_source(name, domain, qualified_name, description, **kwargs):
    # get s3_bucket default type
    entity_type = config.get('aws_s3_bucket', 'entity_type')

    # need to be modified
    template_file_path = base_path + '/entity_source_generation/template/' + entity_type + '.json.j2'

    # generate default value for optional empty attributes
    creator_id = kwargs.get('creator_id', config.get(entity_type, 'creator_id'))
    updator_id = kwargs.get('updator_id', config.get(entity_type, 'updator_id'))
    create_time = kwargs.get('create_time', current_milli_time())
    update_time = kwargs.get('update_time', current_milli_time())
    owner = kwargs.get('owner', config.get(entity_type, 'owner'))
    is_encrypted = kwargs.get('is_encrypted', config.get(entity_type, 'is_encrypted'))
    encryption_type = kwargs.get('encryption_type', config.get(entity_type, 'encryption_type'))
    partner = kwargs.get('partner', config.get(entity_type, 'partner'))
    region = kwargs.get('region', config.get(entity_type, 'region'))

    # populate the template with attributes
    context = {
        # required attributes
        'qualified_name': qualified_name,
        'description': description,
        'domain': domain,
        'name': name,

        # optional attributes
        'created_by': creator_id,
        'updated_by': updator_id,
        'create_time': create_time,
        'update_time': update_time,
        'owner': owner,
        'is_encrypted': is_encrypted,
        'encryption_type': encryption_type,
        'partner': partner,
        'region': region,
    }
    entity_source = populate_template(template_file_path, context)
    return entity_source

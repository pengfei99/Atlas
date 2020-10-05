import os
import jinja2
import time
import configparser

# get current path
base_path = os.getcwd()

# set up config file
config = configparser.ConfigParser()
config.read(base_path + "/config/config.ini")


# get current time
def current_milli_time():
    return int(round(time.time() * 1000))


# get all supported entity types
def get_all_supported_entity_type():
    return ["aws_s3_bucket", "aws_s3_pseudo_dir", "aws_s3_object"]


# get s3_bucket attributes list
def get_all_s3_bucket_supported_attributes():
    return {
        'createdBy': "User id of the entity creator",
        'updatedBy': "User id of the entity updater",
        'createTime': "Creation time of the entity",
        'updateTime': "Last modification time of the entity ",
        'owner': "User id of the entity provider",
        'qualifiedName': "Fully qualified name to access the entity. It must be unique"
                         " Example, s3://minio.lab.sspcloud.fr/donnees-insee  ",
        'encryptionType': 'If data is encrypted, we specify the encryption algorithm here',
        'description': "The description of the entity",
        # 'partner': 'none',
        'domain': "The domain of your s3. Example, minio.lab.sspcloud.fr",
        'isEncrypted': "Indicate if data is encrypted or not, only boolean value is accepted. Example, True, False",
        'name': "The name of the entity, Example, donnees-insee",
        # 'region': 'none',
    }


# jinja2 util function, it takes a jinja2 template and a dict of attributes, then merges them to generate a target file
def populate_template(file_path, context):
    path, file_name = os.path.split(file_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(file_name).render(context)


def generate_s3_bucket_entity_json_source(name, domain, qualified_name, description, **kwargs):
    # get s3_bucket default type
    entity_type = config.get('aws_s3_bucket', 'entity_type')

    # need to be modified
    template_file_path = base_path + '/template/' + entity_type + '.json.j2'

    # generate default value for optional empty attributes
    creator_id = kwargs.get('creator_id', config.get('aws_s3_bucket', 'creator_id'))
    updator_id = kwargs.get('updator_id', config.get('aws_s3_bucket', 'updator_id'))
    create_time = kwargs.get('create_time', current_milli_time())
    update_time = kwargs.get('update_time', current_milli_time())
    owner = kwargs.get('owner', config.get('aws_s3_bucket', 'owner'))
    is_encrypted = kwargs.get('isEncrypted', config.get('aws_s3_bucket', 'isEncrypted'))
    encryption_type = kwargs.get('encryptionType', config.get('aws_s3_bucket', 'encryptionType'))
    partner = kwargs.get('partner', config.get('aws_s3_bucket', 'partner'))
    region = kwargs.get('region', config.get('aws_s3_bucket', 'region'))

    # populate the template with attributes
    context = {
        # required attributes
        'qualifiedName': qualified_name,
        'description': description,
        'domain': domain,
        'name': name,

        # optional attributes
        'createdBy': creator_id,
        'updatedBy': updator_id,
        'createTime': create_time,
        'updateTime': update_time,
        'owner': owner,
        'isEncrypted': is_encrypted,
        'encryptionType': encryption_type,
        'partner': partner,
        'region': region,
    }
    entity_source = populate_template(template_file_path, context)
    return entity_source


def generate_s3_bucket_entity_json_source(name, domain, qualified_name, description, **kwargs):
    # get current path
    base_path = os.getcwd()
    # set up config file
    config = configparser.ConfigParser()
    config.read(base_path + "/config/config.ini")

    # get s3_bucket default type
    entity_type = config.get('aws_s3_bucket', 'entity_type')

    # need to be modified
    template_file_path = base_path + '/template/' + entity_type + '.json.j2'

    # generate default value for optional empty attributes
    creator_id = kwargs.get('creator_id', config.get('aws_s3_bucket', 'creator_id'))
    updator_id = kwargs.get('updator_id', config.get('aws_s3_bucket', 'updator_id'))
    create_time = kwargs.get('create_time', current_milli_time())
    update_time = kwargs.get('update_time', current_milli_time())
    owner = kwargs.get('owner', config.get('aws_s3_bucket', 'owner'))
    is_encrypted = kwargs.get('isEncrypted', config.get('aws_s3_bucket', 'isEncrypted'))
    encryption_type = kwargs.get('encryptionType', config.get('aws_s3_bucket', 'encryptionType'))
    partner = kwargs.get('partner', config.get('aws_s3_bucket', 'partner'))
    region = kwargs.get('region', config.get('aws_s3_bucket', 'region'))

    # populate the template with attributes
    context = {
        # required attributes
        'qualifiedName': qualified_name,
        'description': description,
        'domain': domain,
        'name': name,

        # optional attributes
        'createdBy': creator_id,
        'updatedBy': updator_id,
        'createTime': create_time,
        'updateTime': update_time,
        'owner': owner,
        'isEncrypted': is_encrypted,
        'encryptionType': encryption_type,
        'partner': partner,
        'region': region,
    }
    entity_source = populate_template(template_file_path, context)
    return entity_source

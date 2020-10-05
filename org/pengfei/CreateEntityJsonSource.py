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





# get s3_pseudo_dir attributes list
def get_all_s3_ps_dir_supported_attributes():
    return {
        'name': "Required attribute. "
                "The name of the s3 pseudo dir, Example, RP",
        'qualifiedName': "Required attribute. "
                         " The fully qualified name of the pseudo dir. It must be unique"
                         " Example, s3://minio.lab.sspcloud.fr/donnees-insee/RP/  ",
        'bucket_qualified_name': "Required attribute. "
                                 " The fully qualified name of the s3 bucket which the ps_dir belongs to. "
                                 "Example, s3://minio.lab.sspcloud.fr/donnees-insee",
        'object_prefix': "Required attribute. "
                         " The prefix of all objects in this pseudo dir. "
                         "Example, RP/",
        'description': "The description of the entity",
        'creator_id': "User id of the entity creator",
        'updator_id': "User id of the entity updater",
        'create_time': "Creation time of the entity",
        'update_time': "Last modification time of the entity ",
        'owner': "User id of the entity provider",
        'replicated_to': 'Indicate if this dir is replicated to other path',
        'replicated_from': 'Indicate if this dir is replicated from other path',
        'data_type': 'Specify the the type of data in this dir',
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


def generate_s3_ps_dir_entity_json_source(name, qualified_name, bucket_qualified_name, object_prefix, **kwargs):
    # get current path
    base_path = os.getcwd()
    # set up config file
    config = configparser.ConfigParser()
    config.read(base_path + "/config/config.ini")

    # get s3_ps_dir default type
    entity_type = config.get('aws_s3_pseudo_dir', 'entity_type')
    print(entity_type)
    # need to be modified
    template_file_path = base_path + '/template/' + entity_type + '.json.j2'

    # generate default value for optional empty attributes
    creator_id = kwargs.get('creator_id', config.get(entity_type, 'creator_id'))
    updator_id = kwargs.get('updator_id', config.get(entity_type, 'updator_id'))
    create_time = kwargs.get('create_time', current_milli_time())
    update_time = kwargs.get('update_time', current_milli_time())
    owner = kwargs.get('owner', config.get(entity_type, 'owner'))
    description = kwargs.get('description', config.get(entity_type, 'description'))
    replicated_to = kwargs.get('replicated_to', config.get(entity_type, 'replicated_to'))
    replicated_from = kwargs.get('replicated_from', config.get(entity_type, 'replicated_from'))
    data_type = kwargs.get('data_type', config.get(entity_type, 'data_type'))

    # populate the template with attributes
    context = {
        # required attributes
        'qualified_name': qualified_name,
        'bucket_qualified_name': bucket_qualified_name,
        'object_prefix': object_prefix,
        'name': name,

        # optional attributes
        'created_by': creator_id,
        'updated_by': updator_id,
        'create_time': create_time,
        'update_time': update_time,
        'owner': owner,
        'description': description,
        'replicated_to': replicated_to,
        'replicated_from': replicated_from,
        'data_type': data_type
    }
    entity_source = populate_template(template_file_path, context)
    return entity_source


def generate_s3_object_entity_json_source(name, domain, qualified_name, description, **kwargs):
    # get s3_bucket default type
    entity_type = config.get('aws_s3_bucket', 'entity_type')

    # need to be modified
    template_file_path = base_path + '/template/' + entity_type + '.json.j2'

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

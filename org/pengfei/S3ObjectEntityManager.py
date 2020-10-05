from org.pengfei.utile import *

# get current path
base_path = os.getcwd()

config = init_config()


def generate_s3_object_entity_json_source(name, qualified_name, ps_dir_qualified_name, data_type, owner, description,
                                          **kwargs):
    # get s3_bucket default type
    entity_type = config.get('aws_s3_object', 'entity_type')

    # need to be modified
    template_file_path = base_path + '/template/' + entity_type + '.json.j2'

    # generate default value for optional empty attributes
    creator_id = kwargs.get('creator_id', config.get(entity_type, 'creator_id'))
    updator_id = kwargs.get('updator_id', config.get(entity_type, 'updator_id'))
    create_time = kwargs.get('create_time', current_milli_time())
    update_time = kwargs.get('update_time', current_milli_time())
    compression_type = kwargs.get('compression_type', config.get(entity_type, 'compression_type'))
    size = kwargs.get('size', config.get(entity_type, 'size'))
    replicated_to = kwargs.get('replicated_to', config.get(entity_type, 'replicated_to'))
    replicated_from = kwargs.get('replicated_from', config.get(entity_type, 'replicated_from'))


    # populate the template with attributes
    context = {
        # required attributes
        'name': name,
        'qualifiedName': qualified_name,
        'description': description,
        'ps_dir_qualified_name': ps_dir_qualified_name,
        'data_type':data_type,
        'owner': owner,
        'description': description,

        # optional attributes
        'created_by': creator_id,
        'updated_by': updator_id,
        'create_time': create_time,
        'update_time': update_time,
        'compression_type': compression_type,
        'size': size,
        'replicated_to': replicated_to,
        'replicated_from': replicated_from,

    }
    entity_source = populate_template(template_file_path, context)
    return entity_source

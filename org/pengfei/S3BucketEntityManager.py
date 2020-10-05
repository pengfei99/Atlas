import os
import jinja2


# get current path
base_path = os.getcwd()





# get s3_bucket attributes list
def get_all_supported_attributes():
    return {
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


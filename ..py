""" # ** LOADING IMAGES **
    test_conf_images = [cv2.imread(f'data_especular_crop/test_images/confluente/{image}')/255. for image in os.listdir('data_especular_crop/test_images/confluente/')]
    print(len(test_conf_images))
    train_conf_images = [cv2.imread(f'data_especular_crop/train_images/confluente/{image}')/255. for image in os.listdir('data_especular_crop/train_images/confluente/')]

    test_esp_images = [cv2.imread(f'data_especular_crop/test_images/esparsa/{image}')/255. for image in os.listdir('data_especular_crop/test_images/esparsa/')]
    train_esp_images = [cv2.imread(f'data_especular_crop/train_images/esparsa/{image}')/255. for image in os.listdir('data_especular_crop/train_images/esparsa/')]

    test_int_images = [cv2.imread(f'data_especular_crop/test_images/integra/{image}')/255. for image in os.listdir('data_especular_crop/test_images/integra/')]
    train_int_images = [cv2.imread(f'data_especular_crop/train_images/integra/{image}')/255. for image in os.listdir('data_especular_crop/train_images/integra/')]

    test_rare_images = [cv2.imread(f'data_especular_crop/test_images/rara/{image}')/255. for image in os.listdir('data_especular_crop/test_images/rara/')]
    train_rare_images = [cv2.imread(f'data_especular_crop/train_images/rara/{image}')/255. for image in os.listdir('data_especular_crop/train_images/rara/')]

    # * CREATING LABELS *

    conf_label = np.zeros(len(train_conf_images))
    esp_label = np.ones(len(train_esp_images))
    int_label = 2 * np.ones(len(train_int_images))
    rare_label = 3 * np.ones(len(train_rare_images))

    y_train = np.concatenate((conf_label, esp_label, int_label, rare_label))
    y_train = to_categorical(y_train, 4)
"""
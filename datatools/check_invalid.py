import io_data as SemanticKittiIO

def check_label(path):
    label = SemanticKittiIO._read_label_SemKITTI(path)
    return label

def check_invalid(path):
    invalid = SemanticKittiIO._read_invalid_SemKITTI(path)
    return invalid

def check_occluded(path):
    occluded = SemanticKittiIO._read_occluded_SemKITTI(path)
    return occluded

# def visualize_label(label):
#     import matplotlib.pyplot as plt
#     plt.imshow(label)
#     plt.show()



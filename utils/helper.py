import pickle

def save(data, path):
    f = open('./'+path,'wb')
    pickle.dump(data,f)
    f.close()
    
def load(path):
    f = open('./'+path,'rb')
    fres = pickle.load(f)  
    f.close()
    return fres

def show_model_plot(model_h, loss_text_offset=(.95, .02), acc_text_offset=(.95, 1.1), xoffset=.6):
    import matplotlib.pyplot as plt
    import numpy as np
    from keras.models import load_model
    import matplotlib.patches as mpatches
    
    history = model_h['history']
    h_params = model_h['hyper_parameters']

    green_color = '#c4e199'

    acc = np.array(history.history['acc'] if history.history.get('accuracy') == None else history.history['accuracy'])*100
    val_acc = np.array(history.history['val_acc'] if history.history.get('val_accuracy') == None else history.history['val_accuracy'])*100
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)

    fig, ax = plt.subplots(3, 2)
    fig.set_size_inches(20, 5)

    #---------------------------------
    xa1 = plt.subplot(121)
    plt.plot(epochs, acc, 'c--', label='Training acc')
    plt.plot(epochs, val_acc, 'co-', label='Validation acc')
    plt.title('Training and validation accuracy')
    print(plt.xlabel)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.xticks(range(1,h_params['epochs']+1, 2))
    plt.grid(alpha=.3)
    plt.legend()

    for i, v in enumerate(val_acc):
        rvalue = int(round(v))

        if i%2==0: pad = acc_text_offset[1]
        else: pad = -acc_text_offset[1]

        plt.text(i + acc_text_offset[0],
            v + pad ,
            str(rvalue),
            color='red',
            alpha=.4,
            fontweight='normal')
    #plt.text(np.argmax(val_acc)+acc_max_offset[0],
    #         np.max(val_acc)+acc_max_offset[1],
    #         'max acc: ' + str(round(np.max(val_acc), 3)),
    #         color='green',
    #         alpha=1,
    #         fontweight='bold',
    #         fontsize=15)
    #plt.text(np.argmax(val_acc)+acc_max_offset[0],
    #         np.max(val_acc)+acc_max_offset[1]+acc_max_offset[2],
    #         'epoch: ' + str(np.argmax(val_acc)),
    #         color='green',
    #         alpha=1,
    #         fontweight='bold',
    #         fontsize=15)
    el = mpatches.Ellipse((epochs, val_acc), 0.3, 0.4, angle=30, alpha=0.2)
    ymax = np.max(val_acc)
    xmax = np.argmax(val_acc)+1
    xa1.annotate('max acc: ' + str(round(np.max(val_acc), 1)) + '\n' + 'epoch: ' + str(np.argmax(val_acc)+1),
                 xy=(xmax, ymax),
                 xytext=(len(acc)/4, min(acc)+(max(acc)-min(acc))/5),
                 bbox=dict(boxstyle='round,pad=0.2',
                           fc=green_color,
                           alpha=0.8),
                 arrowprops=dict(arrowstyle='fancy',
                                color=green_color,
                                patchB=el,
                                shrinkB=5,
                                connectionstyle='arc3,rad=0.3',
                                ),
                 fontsize=20,
                ) 

    #---------------------------------
    xa2 = plt.subplot(122)    
    plt.plot(epochs, loss, 'm--', label='Training loss')
    plt.plot(epochs, val_loss, 'mo-', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.xticks(range(1,h_params['epochs']+1, 2))
    plt.grid(alpha=.3)
    plt.legend()

    for i, v in enumerate(val_loss):
        rvalue = round(v, 2)

        if i%2==0: pad = loss_text_offset[1]
        else: pad = -loss_text_offset[1]

        plt.text(i + loss_text_offset[0],
            v + pad,
            str(rvalue),
            color='red',
            alpha=.4,
            fontweight='normal')

    #plt.text(np.argmin(val_loss)+loss_min_offset[0],
    #         np.min(val_loss)+loss_min_offset[1],
    #         'min loss: ' + str(round(np.min(val_loss), 3)),
    #         color='green',
    #         alpha=1,
    #         fontweight='bold',
    #         fontsize=15)
    #plt.text(np.argmin(val_loss)+loss_min_offset[0],
    #         np.min(val_loss)+loss_min_offset[1]+loss_min_offset[2],
    #         'epoch: ' + str(np.argmin(val_loss)),
    #         color='green',
    #         alpha=1,
    #         fontweight='bold',
    #         fontsize=15)

    el = mpatches.Ellipse((epochs, val_acc), 0.3, 0.4, angle=30, alpha=0.2)
    ymin = np.min(val_loss)
    xmin = np.argmin(val_loss)+1
    xa2.annotate('min loss: ' + str(round(np.max(val_loss), 3)) + '\n' + 'epoch: ' + str(np.argmin(val_loss)+1), 
                 xy=(xmin, ymin),
                 xytext=(len(loss)/4, min(loss)+(max(loss)-min(loss))/1.5),
                 bbox=dict(boxstyle='round,pad=0.2',
                           fc=green_color,
                           alpha=0.8),
                 arrowprops=dict(arrowstyle='fancy',
                                color=green_color,
                                patchB=el,
                                shrinkB=5,
                                connectionstyle='arc3,rad=-0.3',
                                ),
                 fontsize=20,
                )

    plt.show()
    return xa1, xa2
    
def autolabel(rects, ax):
    import matplotlib.pyplot as plt
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')    
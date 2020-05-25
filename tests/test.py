import unittest


class TestPrettyConfMat(unittest.TestCase):
    def test_data_class(self):
        """ test function with y_test (actual values) and predictions (predic) """
        #data
        y_test = np.array([1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5])
        predic = np.array([1,2,4,3,5, 1,2,4,3,5, 1,2,3,4,4, 1,4,3,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,3,3,5, 1,2,3,3,5, 1,2,3,4,4, 1,2,3,4,1, 1,2,3,4,1, 1,2,3,4,1, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5])
        """
        Examples to validate output (confusion matrix plot)
            actual: 5 and prediction 1   >>  3
            actual: 2 and prediction 4   >>  1
            actual: 3 and prediction 4   >>  10
        """
        columns = []
        annot = True
        cmap = 'Oranges'
        fmt = '.2f'
        lw = 0.5
        cbar = False
        show_null_values = 2
        pred_val_axis = 'y'
        fz = 12
        figsize = [9, 9]
        if(len(y_test) > 10):
            fz = 9; figsize=[14, 14]
        plot_confusion_matrix_from_data(y_test, predic, columns,
        annot, cmap, fmt, fz, lw, cbar, figsize, show_null_values, pred_val_axis)

    def test_cm(self):
        #test function with confusion matrix done
        array = np.array( [[13,  0,  1,  0,  2,  0],
                        [ 0, 50,  2,  0, 10,  0],
                        [ 0, 13, 16,  0,  0,  3],
                        [ 0,  0,  0, 13,  1,  0],
                        [ 0, 40,  0,  1, 15,  0],
                        [ 0,  0,  0,  0,  0, 20]])
        #get pandas dataframe
        df_cm = DataFrame(array, index=range(1, 7), columns=range(1, 7))
        #colormap: see this and choose your more dear
        cmap = 'PuRd'
        pretty_plot_confusion_matrix(df_cm, cmap=cmap)


if __name__ == '__main__':
    unittest.main()

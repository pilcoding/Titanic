import pandas as pd

class Data():
    """
    Class representing the data of data challenge, implementing classic functions
    """

    def __init__(self,x_train: pd.DataFrame = None, y_train: pd.DataFrame = None, x_test: pd.DataFrame = None, 
                    data_path: str = "../data/", submission_path: str = "../submission/"):
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.data_path = data_path
        self.submission_path = submission_path

    def __str__(self):
        if self.x_train != None:
            return self.x_train.head(3)
        return "Data not loaded"

    def loadData(self, path: str = None, file_ext: str = ".csv", y_col: str = "", head: int = 0):
        """
        Try to load data from the data path. 
        """
        if path != None:
            self.data_path = path

        try:

            self.x_train = pd.read_csv(self.data_path + "train" + file_ext,delimiter= ",",header= head)

            if y_col:
                self.y_train = self.x_train[y_col].copy()

        except Exception as e:
            print(f"An error occurred: {e}")

        try:

            self.x_test = pd.read_csv(self.data_path + "test" + file_ext,delimiter= ",",header= head)
        except Exception as e:
            print(f"An error occurred: {e}")


    def drop_col(self,cols):
        """
        Dropping columns of the dataset

        """
        for df in (self.x_train,self.x_test):
            for col in cols:
                try: 
                    df.drop(col,axis=1,inplace=True)
                except Exception as e:
                    print(f"An error occurred: {e}")

    def set_categorial(self,cols):
        """
        Setting colunms as categorials
        """

        for df in (self.x_test,self.x_train):
            try:
                df[cols] = df[cols].astype('category')
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_numerical(self):
        """
        Return the columns with a numerical dtype
        """
        result = []
        for col in self.x_train.columns:
            if self.x_train[col].dtype in (int,float):
                result.append(col)
        return result

    def get_categorial(self):
        """
        Return the categorial columns
        """
        result = []
        for col in self.x_train.columns:
            if self.x_train[col].dtype == "category":
                result.append(col)
        return result

    def code_col(self,cols,codes: dict):
        """
        Encoding categorial variables
        """
        try:

            for df in (self.x_train,self.x_test):
                for col in cols:

                    if col not in codes:
                        df[col] = df[col].cat.codes
                    else:
                        df[col] = df[col].map(codes[col])

        except Exception as e:
            print(f"An error occurred: {e}")

from v1.models import InputData, OutputData
from .serializer import *
from rest_framework import parsers, permissions, views, status, viewsets
from rest_framework.response import Response
import pandas as pd
from datetime import datetime, timedelta

"""
A Few Utility Functions for managing the datetime object
"""
def str_to_datetime(s_date, s_time):
    return datetime.strptime(s_date + ' ' + s_time, '%d/%m/%y %H:%M:%S') + timedelta(hours=6) # Add 6 hours to convert to UTC, SInce my PC is at GMT+6

def date_to_str(datetime):
    return datetime.strftime('%Y%m%d')

"""
Created a FileUploadView that will take the file and process the data and create corresponding objects in the database.
    - The file is uploaded as a CSV file.
    - The CSV file is parsed and the data is stored in a pandas dataframe.
    - The dataframe is iterated over and the data is stored in the database.
"""
class FileUploadView(views.APIView):
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        if not file:
            return Response({'message': 'Error! No file received.'}, status=status.HTTP_400_BAD_REQUEST)
        df = pd.read_csv(file)
        for _ in range(len(df.index)):
            InputData.objects.create(
                sl = df.iloc[_]['Sl'],
                date = df.iloc[_]['Date'],
                time = df.iloc[_]['Time'],
                product = df.iloc[_]['Product'],
                side = df.iloc[_]['Side'],
                qty = df.iloc[_]['Qty'],
                exe_price = df.iloc[_]['Exe Price'],
                acct = df.iloc[_]['Acct']
            )
            dt = str_to_datetime(df.iloc[_]['Date'], df.iloc[_]['Time'])
            OutputData.objects.create(
                sl = df.iloc[_]['Sl'],
                transaction_at = dt,
                timestamp = int(dt.timestamp()),
                product = df.iloc[_]['Product'],
                qty = df.iloc[_]['Qty'],
                price = float(df.iloc[_]['Exe Price']),
                side = df.iloc[_]['Side'],
                acct = df.iloc[_]['Acct'],
                group = "_".join([df.iloc[_]['Acct'], df.iloc[_]['Product'], date_to_str(dt)])
            )
        return Response({'message': 'File has been processed'}, status=status.HTTP_201_CREATED)

"""
A ModelViewSet for the InputData model
    - Contains a list of all the InputData objects
        - The list can be filtered by sl, product, side, acct, group, timestamp
    - Can create new InputData objects
    - Can update existing InputData objects
    - Can delete existing InputData objects
    - Can view individual InputData objects by their id.
"""

class OutputDataViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OutputDataSerializer
    def get_queryset(self):
        res = OutputData.objects.all()
        if self.request.query_params.get('sl'):
            res = res.filter(sl=self.request.query_params.get('sl'))
        if self.request.query_params.get('product'):
            res = res.filter(product=self.request.query_params.get('product'))
        if self.request.query_params.get('side'):
            res = res.filter(side=self.request.query_params.get('side'))
        if self.request.query_params.get('acct'):
            res = res.filter(acct=self.request.query_params.get('acct'))
        if self.request.query_params.get('group'):
            res = res.filter(group=self.request.query_params.get('group'))
        if self.request.query_params.get('timestamp'):
            res = res.filter(timestamp=self.request.query_params.get('timestamp'))
        return res
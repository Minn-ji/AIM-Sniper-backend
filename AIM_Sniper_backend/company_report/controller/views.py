import json

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from company_report.entity.models import CompanyReport
from company_report.serializers import CompanyReportSerializer
from company_report.service.companyReport_service_impl import CompanyReportServiceImpl


class CompanyReportView(viewsets.ViewSet):
    queryset = CompanyReport.objects.all()
    companyReportService = CompanyReportServiceImpl.getInstance()

    def list(self, request):
        companyReportList = self.companyReportService.list()
        # print('companyReportList : ', companyReportList)
        serializer = CompanyReportSerializer(companyReportList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data
            companyReportTitleImage = request.FILES.get('companyReportTitleImage')
            companyReportName = data.get('companyReportName')
            companyReportPrice = data.get('companyReportPrice')
            companyReportCategory = data.get('companyReportCategory')
            content = data.get('content')

            if not all([companyReportName, companyReportPrice, companyReportCategory,content, companyReportTitleImage]):
                return Response({'error': '모든 내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            self.companyReportService.createCompanyReport(companyReportName, companyReportPrice, companyReportCategory,content, companyReportTitleImage)

            serializer = CompanyReportSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readCompanyReport(self, request, pk=None):
        companyReport = self.companyReportService.readCompanyReport(pk)
        serializer = CompanyReportSerializer(companyReport)
        return Response(serializer.data)

    def deleteCompanyReport(self,request,pk=None):
        self.companyReportService.deleteCompanyReport(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


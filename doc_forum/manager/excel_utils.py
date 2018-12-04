# -*- coding: utf-8 -*-
from django.http import HttpResponse
import xlsxwriter

from doc_forum.agreement.models import Agreeement
from doc_forum.proposal.models import Proposal

def WriteToExcel(is_agre):
    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO

    a_list = []
    obj_agre =Agreeement.objects.all()
    obj_pro =Proposal.objects.all()

    if is_agre:
        obj =obj_agre
    else:
        obj =obj_pro
    for g in obj:
        print g
        print "Exportando..."
        a_list.append({'obj': g})


    if is_agre:
        data = sorted(a_list, key=lambda k: k['obj'].legasl_instrument, reverse=True)
    else:
        data = sorted(a_list, key=lambda k: k['obj'].title, reverse=True)

    output = StringIO.StringIO()

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('new-spreadsheet')


    if is_agre:
        worksheet.write(0, 0, 'Num Programa')
        worksheet.write(0, 1, 'Legal')
        worksheet.write(0, 2, 'Clasificacion del Documento')
        worksheet.write(0, 3, 'Numero de registro')
        worksheet.write(0, 4, 'Intitucion contraparte')
        worksheet.write(0, 5, 'Campo subcripcion')
        worksheet.write(0, 6, 'Sector contraparte')
        worksheet.write(0, 7, 'Institucion contraparte')
        worksheet.write(0, 8, 'Descripcion')
        #worksheet.write(0, 9, 'Fecha de firma')
        #worksheet.write(0, 10, 'Fecha Inicio')
        #worksheet.write(0, 11, 'Fecha Fin')
        #worksheet.write(0, 12, 'Duracion')
        #worksheet.write(0, 13, 'Vigencia')
        worksheet.write(0, 9, 'Modal')
        #worksheet.write(0, 1, 'Version')
    else:
        worksheet.write(0, 0, 'Fondo')
        worksheet.write(0, 1, 'Proyecto')
        worksheet.write(0, 2, 'Titulo')
        worksheet.write(0, 3, 'Responsable tecnico')
        worksheet.write(0, 4, 'Monto solicitado')
        worksheet.write(0, 5, 'Monto Autorizado')
        worksheet.write(0, 6, 'Monto Transeferido')
        worksheet.write(0, 7, 'Observaciones')
        # worksheet.write(0, 8, 'Vigencia')


    # call_background = models.CharField(verbose_name = "Fondo/Convocatoria", max_length=250)
    #project = models.IntegerField(verbose_name = "Proyecto", max_length=250)
    #title = models.CharField(verbose_name = "Titulo", max_length=250)
    #techical_responsible = models.CharField(verbose_name = "Responsable Técnico", max_length=250)
    #request_amount = models.DecimalField(verbose_name = "Monto Solicitado", max_digits=6, decimal_places=3)
    #authorized_amount = models.DecimalField(verbose_name = "Monto Autorizado", max_digits=6, decimal_places=3)
    #transfer = models.DecimalField(verbose_name = "Transferencia", max_digits=6, decimal_places=3)
    #observation = models.TextField(verbose_name='Observaciones', max_length=250)
    #validity_date = models.DateTimeField(verbose_name = "Vigencia",default=datetime.now,help_text="Vigencia")
    #proposal_name = models.CharField(verbose_name = "Propuesta", max_length=250, null=True, blank=True)
    #docfile_proposal = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona un documento para la propuesta ",null=True, blank=True)
    #docto_name_pro_acept = models.CharField(verbose_name = "Documento Aceptado", max_length=250, null=True, blank=True)
    ##docto_pro_acept = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento Aceptado",null=True, blank=True)
    #docto_legal_pro_name = models.CharField(verbose_name = "Documento Legal", max_length=250, null=True, blank=True)
    #docto_legal_pro = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento Legal",null=True, blank=True)

    for i, row in enumerate(obj):
        print i
        x = 1 +i

        if is_agre:
            worksheet.write(x, 0, row.prog_number)
            worksheet.write(x, 1, row.legasl_instrument)
            worksheet.write(x, 2, row.document_classification)
            worksheet.write(x, 3, row.registration_number)
            worksheet.write(x, 4, row.conterpart_institution_acroniym)
            worksheet.write(x, 5, row.subscription_field)
            worksheet.write(x, 6, row.conterpart_sector)
            worksheet.write(x, 7, row.conterpart_institution.name)
            worksheet.write(x, 8, row.description)
            #worksheet.write(x, 9, row.signature_date)
            #worksheet.write(x, 10, row.start_date)
            #worksheet.write(x, 11, row.end_date)
            #worksheet.write(x, 12, row.duration)
            #worksheet.write(x, 13, row.status)
            worksheet.write(x, 9, row.modal)
            #worksheet.write(2, i, row.version_docto)

            #worksheet.write(1, i, getattr(str(row['obj'].conterpart_institution_acroniym), 'attribute1 not available'))
            #worksheet.write(2, i, getattr(str(row['obj'].registration_number), 'attribute2 not available'))
        else:
            worksheet.write(x, 0, row.call_background)
            worksheet.write(x, 1, row.project)
            worksheet.write(x, 2, row.title)
            worksheet.write(x, 3, row.techical_responsible)
            worksheet.write(x, 4, row.request_amount)
            worksheet.write(x, 5, row.authorized_amount)
            worksheet.write(x, 6, row.transfer)
            worksheet.write(x, 7, row.observation)
            # worksheet.write(x, 8, row.validity_date)

    workbook.close()
    if is_agre:
        file_name = "ReporteConvenio.xlsx"
    else:
        file_name = "ReportePropuesta.xlsx"

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename='+file_name


    return response

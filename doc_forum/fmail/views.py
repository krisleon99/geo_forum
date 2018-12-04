# -*- encoding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from time import sleep

from doc_forum.fmail.forms import SendFmail_Form, SendFmail_User, SendFmail_Dimension, SaveFmailHistory, UpdateFmailHistory
from doc_forum.fmail.Temporizador import Temporizador
from doc_forum.fmail.models import SendFmail, TokenF
from doc_forum.forum.models import Topic

# Create your views here.
"""
Este metodo es para seguir un tema de discución y que las notificaciones le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def follow_forum(request, id_topic):
    if id_topic:
        if request.user.is_authenticated():
            user_id = request.user.id
            now = timezone.now()
            formulario = SendFmail_Form({'user_owner': user_id, 'topic': id_topic, 'status': 1, 'creation_date': now})
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect(reverse("view_topic", kwargs={'id_topic':id_topic}))
    return render_to_response('topics_index.html', context_instance=RequestContext(request))

"""
Este metodo es para dejar de seguir un tema de discución y que las notificaciones ya no le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def leave_forum(request, fmail):
    if fmail:
        obj = get_object_or_404(SendFmail, id=fmail)
        user_id = 1000
        if request.user.is_authenticated():
            if obj:
                obj.delete()
                return HttpResponseRedirect(reverse("view_topic", kwargs={'id_topic':obj.topic.id}))
    return render_to_response('topics_index.html', context_instance=RequestContext(request))

"""
Este metodo es para seguir a unusuario y cada vez que suba un docto las notificaciones le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def follow_user(request, id_user):
    user_id = request.user.id
    now = timezone.now()
    formulario = SendFmail_User({'user_owner': user_id, 'user_follow': id_user, 'status': 1, 'creation_date': now})
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect(reverse("user_detail", kwargs={'id_user':id_user}))
    topics = Topic.objects.all()
    return render_to_response('topics_index.html', context_instance=RequestContext(request))


"""
Este metodo es para dejar de seguir un tema de discución y que las notificaciones ya no le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def leave_user(request, fmail, id_user):
    if fmail:
        obj = get_object_or_404(SendFmail, id=fmail)
        user_id = 1000
        if request.user.is_authenticated():
            if obj:
                obj.delete()
                return HttpResponseRedirect(reverse("user_detail", kwargs={'id_user':id_user}))
    return render_to_response('topics_index.html', context_instance=RequestContext(request))

"""
Este metodo es para seguir una dimesón y que las notificaciones le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def follow_dimension(request):
    if request.user.is_authenticated():
        #Todo get dimension with method GET:
        dimension = request.GET.get('dimension', '')
        user_id = request.user.id
        now = timezone.now()
        formulario = SendFmail_Dimension({'user_owner': user_id, 'dimension':dimension, 'status': 1, 'creation_date': now})
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse("agreement_and_proposal"))
    return render_to_response('topics_index.html', context_instance=RequestContext(request))

"""
Este metodo es para dejar de seguir una dimensión y que las notificaciones ya no le lleguen al usuario por correo
"""
@login_required(login_url='/manager/ingresar')
def leave_dimension(request, fmail):
    if fmail:
        obj = get_object_or_404(SendFmail, id=fmail)
        if request.user.is_authenticated():
            if obj:
                obj.delete()
                return HttpResponseRedirect(reverse("agreement_and_proposal"))
    return render_to_response('topics_index.html', context_instance=RequestContext(request))

def ejecutar():
    print('Función ejecutada desde hilo')

"""
Método generico para que enviar un e-mail de alerta de modificación de algún objeto: FORO, USER, or DIMENSION.
Requiere de 4 parametros, 1.- activity: puede ser el usuario, el titulo del foro o la dimención, según sea el caso.
2.- authorized es una constante en la cual sabemos que tipo de objeto es: USER, FORUM, or DIMENSION.
3.- user_id: Usuario al cual se le enviará el correo.
4.- token; es la URL que se le manda vía e-mail al usuario para acceder a la plataforma, esta puede variar, de acuerdo al objeto.
"""
def send_fmail():
    mail =""
    try:
        tok_preparing = TokenF.objects.filter(status=0)
        for tok in tok_preparing:
            if tok.comment_html:
                print("tiene ,mail"+str(tok.comment_html))
                EMAIL_RECEPT = tok.comment_html
                subject, from_email, to = tok.subject, settings.THEME_ACCOUNT_CONTACT_EMAIL, EMAIL_RECEPT
                msg = EmailMultiAlternatives(subject, tok.body, from_email, [to])
                msg.attach_alternative(tok.body, "text/html")
                msg.send()
                tok_unique = get_object_or_404(TokenF, id=tok.id)
                if tok_unique:
                    form_t = UpdateFmailHistory({'status':1}, instance=tok_unique)
                    form_t.save()
                print("send")
        # us_m = get_object_or_404(User, id=user_id)
        # mail = us_m.email
        # print("tiene ,mail"+str(mail))
        # if mail:
        #     print("Se va enviar un e-mail, ")
        #     if authorized in "FORUM":
        #         SUBJECT_AUTHORIZED_COMMENTS = "SUSCRIPCIÓN DE FORO: "+str(activity)
        #         CONTENT= "relacionada con el foro: "+str(activity)
        #     if authorized in "USER":
        #         SUBJECT_AUTHORIZED_COMMENTS = "ACTIVIDAD DE USUARIO: "+str(activity)
        #         CONTENT = "relacionada con el usuario: "+str(activity)
        #     if authorized in "DIMENSION":
        #         SUBJECT_AUTHORIZED_COMMENTS = "ACTIVIDAD DE DIMENSIÓN: "+str(activity)
        #         CONTENT = "relacionada con la dimensión: "+str(activity)
        #     EMAIL_RECEPT = mail
        #     subject, from_email, to = SUBJECT_AUTHORIZED_COMMENTS, settings.THEME_ACCOUNT_CONTACT_EMAIL, EMAIL_RECEPT
        #     text_content = '<strong>Estimad@ '+str(us_m.username)+'</strong> por este medio se le informa que hubo actividad:'
        #     html_content = '<strong>Estimad@ '+str(us_m.username)+'</strong> por este medio se le informa que hubo actividad:<div>'\
        #                    +str(CONTENT)+'</div><h3>Puede vizualizarlo <a href="'+str(token)+'">aquí</a> </h3>'
        #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #     msg.attach_alternative(html_content, "text/html")
        #     msg.send()
        #     print("send")
        #     return "Send"
        # else:
        #     return "No send"
    except TokenF.DoesNotExist:
        print("El usuario No tiene mail")
        return "No send"
"""
Build the token for send email from forum
"""
def build_token_f(id_forum):
    try:
        site1 = Site.objects.get(id=1).domain
        token = site1+"/forum/view/"+str(id_forum)+""
        return token
    except Site.DoesNotExist:
        print("El sitio no existe")
        return "Invalid"

"""
Build the token for send email from doctos
"""
def build_token_docto(obj):
    try:
        site1 = Site.objects.get(id=1).domain
        token = site1+"/agreementgesp/"+str(obj)
        return token
    except Site.DoesNotExist:
        print("El sitio no existe")
        return "Invalid"
"""
Valid object type, forum, user or dimension
"""
def locate_object_f(obj, obj_id):
    try:
        obj_f = None
        str_f = ""
        if obj in "FORUM":
            obj_f = get_object_or_404(Topic, id=obj_id).title
            str_f = ""+obj_f
        if obj in "DIMENSION":
            if '1' in str(obj_id): # toDo, no hay una bd de dimensioones
                str_f = "GENERAL"
            elif '2' in str(obj_id):
                str_f = "CONTEXTO TERRITORIAL"
            elif '3' in str(obj_id):
                str_f = "DIMENSIÓN GEOPOLÍTICA"
            elif '4' in str(obj_id):
                str_f = "DIMENSIÓN DE SEGURIDAD"
            elif '5' in str(obj_id):
                str_f = "DIMENSIÓN DE INSTITUCIONAL"
            elif '6' in str(obj_id):
                str_f = "DIMENSIÓN LABORAL Y ECONÓMICA"
            elif '7' in str(obj_id):
                str_f = "DIMENSIÓN SOCIAL Y CULTURAL"
            elif '8' in str(obj_id):
                str_f = "DIMENSIÓN ASENTAMIENTOS HUMANOS, CIUDADES Y MARCO AMBIENTAL"
        if obj in "USER":
            obj_f = get_object_or_404(User, id=obj_id).username
            str_f = ""+obj_f
        return str_f
    except Site.DoesNotExist:
        print("El sitio no existe")
        return "Invalid"
"""
este metodo guarda un el token
 """
def save_token_fmail(request,id_comment, id_comment_to_comment, id_user, token):
    try:
        is_autorized =False
        id_token = 0
        #comment_last = CommentWithColumn.objects.latest('submit_date')
        #print("guardara?"+str(id_comment))
        formulario = TokenAuthorizedCommentsForm({'id_comment': id_comment, 'id_comment_to_comment':id_comment_to_comment, 'token':token,'author':id_user, 'is_autorized':is_autorized})
        if formulario.is_valid():
            formulario.save()
            tok = TokenAuthorizedComments.objects.latest('creation_date')
            id_token = tok.id
            return id_token
        else:
            return 0
            print(" don saved")
    except ValueError:
        print("Error valor no numerico")
        return 0
    return id_token

"""
Test email
"""
def test_email(request):
    try:
        print "mail de prueba"
        site1 = Site.objects.get(id=1).domain
        token = site1+"forum/view/"
        send_mail(
            'test',
            'Este correo es de prueba.',
            'chokokriss97@gmail.com',
            ['christian.leon.alvarez@gmail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse("forum_web"))
    except Site.DoesNotExist:
        print("No se pudo enviar el correo por que el sitio no existe")
        return "Invalid"

"""
este metodo es para guardar el historial de los e-mails que se enviarán a los respectivos usuarios
"""
def save_fmail(activity, authorized, user_id, token, send):
    mail =""
    try:
        us_m = get_object_or_404(User, id=user_id)
        mail = us_m.email
        if mail:
            SUBJECT_AUTHORIZED_COMMENTS = "some"
            now = timezone.now()
            if authorized in "FORUM":
                SUBJECT_AUTHORIZED_COMMENTS = "SUSCRIPCIÓN DE FORO: "+str(activity)
                CONTENT= "relacionada con el foro: "+str(activity)
            if authorized in "USER":
                SUBJECT_AUTHORIZED_COMMENTS = "ACTIVIDAD DE USUARIO: "+str(activity)
                CONTENT = "relacionada con el usuario: "+str(activity)
            if authorized in "DIMENSION":
                SUBJECT_AUTHORIZED_COMMENTS = "ACTIVIDAD DE DIMENSIÓN: "+str(activity)
                CONTENT = "relacionada con la dimensión: "+str(activity)
            html_content = '<strong>Estimad@ '+str(us_m.username)+'</strong> por este medio se le informa que hubo actividad:<div>'\
                           +str(CONTENT)+'</div><h3>Puede vizualizarlo <a href="'+str(token)+'">aquí</a> </h3>'
            form_his = SaveFmailHistory({'user': us_m.id, 'send':send,'subject': SUBJECT_AUTHORIZED_COMMENTS, 'body': html_content, 'token':token,'comment_html':mail,'creation_date': now, 'status':0, 'is_autorized':0})
            if form_his.is_valid():
                form_his.save()
            return "Send"
        else:
            return "No send"
    except User.DoesNotExist:
        print("El usuario No tiene mail")
        return "No send"

"""
Metodo para comenzar el hilo para que envia los correos para avisar a los usuarios de actividad en sus cuentas.
"""
@login_required(login_url='/manager/ingresar')
def start_stop_thread(request):
    try:
        t = Temporizador('07:00:00',1,send_fmail)# Instanciamos nuestra clase Temporizador
        t.start() #Iniciamos el hilo
        sleep(2)
        for _ in range(10):
            print('Imprimiendo desde hilo principal')
            sleep(2)
        return HttpResponseRedirect(reverse("list_agreementgesp"))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("list_agreementgesp"))

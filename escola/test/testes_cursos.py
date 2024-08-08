from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user

class CursosTestCase(APITestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
        email='asdf@gmail.com',
        password='123',
        username='matheus'
        )
        self.client.force_authenticate(self.user)
        #self.client.force_login(username=self.user.username, password=self.user.password)

        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT2', descricao = 'Curso teste 2', nivel = 'A'
        )
    
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para cadastrar os cursos."""
        data = {
            'codigo_curso': 'CTT3', 'descricao': 'Curso teste 3', 'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar cursos."""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso."""
        data = {
            'codigo_curso': 'CTT1', 'descricao': 'Curso teste alterado', 'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#tem q tirar a page size em setting na pasta setup
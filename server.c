#include <sys/types.h> 
#include <sys/socket.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

int hebras[10];
char x, y;



void control(void *par_idx){
        int idx = (int)((int *)par_idx);  
        int largo_leido, t, u, d=10, cc=0; 
        char car_ant=0;
        char buffer[1024];
        srand(time(NULL));
	 printf("H:%d\n", idx);

	//envia id del jugador (indice del array de conexiones)
        bzero(buffer, sizeof(buffer));
        sprintf(buffer,"%d\n", idx);
        write(hebras[idx], buffer, sizeof(buffer));

        largo_leido = read(hebras[idx], buffer, sizeof(buffer));
        while (largo_leido>0)
        {
		if (car_ant!=buffer[0])
			printf("H%d key:%d (%c)\n", idx, buffer[0], buffer[0]);
		car_ant = buffer[0];
		if (idx==0){
	              if (buffer[0]=='w') {y='w';}
        	       if (buffer[0]=='s') {y='s';}
                	if (buffer[0]=='d') {y='d';}
                	if (buffer[0]=='a') {y='a';}
			if (buffer[0]=='S') {y='S';}
		} 
		else {
                     if (buffer[0]=='w') {x='w';}
                     if (buffer[0]=='s') {x='s';}
                     if (buffer[0]=='d') {x='d';}
                     if (buffer[0]=='a') {x='a';}
			if (buffer[0]=='S') {x='S';}
                }
		bzero(buffer, sizeof(buffer));
		sprintf(buffer,"%d;%d;", x, y);
		write(hebras[idx], buffer, sizeof(buffer));
                largo_leido = read(hebras[idx], buffer, sizeof(buffer));
        } 
        printf("Cierra conexion\n");
        close(hebras[idx]);
}



int main(int argc, char *argv[])
{
	struct  sockaddr_in server;
	int largo_leido, largo_socket, nuestro_socket, conexion;
	pthread_t threads[10];
	int idx=0;

	
	nuestro_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (nuestro_socket < 0) 
	{
		perror ("ERROR: No se puede crear socket.");
		exit (1);
	}

	 
	bzero(&server, sizeof(server)); 

	server.sin_family		= AF_INET; 
	server.sin_addr.s_addr	= INADDR_ANY;
	server.sin_port			= htons(atoi(argv[1])); 
	
	if (bind(nuestro_socket, (struct  sockaddr *)&server, sizeof(server)) < 0)
	{
		close(nuestro_socket);
		perror("ERROR: No se puede hacer bind del socket.");
		exit(1);
	}

	if (listen(nuestro_socket, 5) < 0) 
	{
		perror ("ERROR: No se puede escuchar.");
		exit (1);
	}
	
	largo_socket = sizeof (struct sockaddr_in);

	//****************************************************
	/*
	 * Esta es la parte en donde se debe trabajar!!!
	 */
	while(1){ 
		printf("Servidor activo, esperando conexion... %d\n", idx);
		hebras[idx] = accept(nuestro_socket, (struct  sockaddr *)&server, &largo_socket);
		printf("Conexi�n aceptada desde: %s\n", inet_ntoa(server.sin_addr));
        	pthread_create(&threads[idx], NULL,(void *)&control, (void *)idx);
		idx++;
        }		
        close(nuestro_socket);
	//****************************************************

	return 0;
}


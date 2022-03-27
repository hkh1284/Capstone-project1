# 업비트의 가상화폐 데이터를 NAS에 저장

### 0. NAS의 특정 디렉토리에 데이터를 축적하려면 어떻게 해야하는가?
#### NFS를 사용해 NAS의 특정 디렉토리를 내 노트북의 파일시스템의 일부로 마운트
##### NFS(Network File System)란? 
- 네트워크 상에 연결된 다른 컴퓨터의 하드디스크를 내 컴퓨터의 하드디스크처럼 사용하는 것.

- 즉, 클라이언트(내 노트북)가 원격지 컴퓨터(NAS)에 있는 파일을 클라이언트에 있는 파일처럼 
마음대로 검색/수정/저장할 수 있도록 해주는 클라이언트/서버 구조의 응용프로그램

- 클라이언트에는 NFS클라이언트 설치, 서버에는 NFS서버 설치 해야한다.

### 1. NFS설치
#### <NFS 서버>
- NFS 관련 패키지 설치
sudo apt install nfs-kernel-server (Ubuntu)

- 마운트를 허가할 디렉토리와 마운트를 허가할 호스트 목록을 설정
vi /etcexports [허가할 디렉토리] [허가할 호스트 ip주소](옵션1, 옵션2, ...)   
// rw : 읽기쓰기가능, ro : 읽기만 가능, noaccess : 액세스거부
// root_squach : 클의 root가 서버의 root권한획득 막음 
// no_root_squach : 클의 root와 서버의 root권한을 동일하게 함
// sync : 파일시스템이 변경되면 즉시 동기화

- NFS 실행
service nfs-kernel-server restart (Ubuntu)

- NFS 맵핑 정보확인
rpcinfo -p [맵핑정보를 확인하고자하는 특정ip]

#### <NFS 클라이언트>
- NFS 관련 패키지 설치
sudo apt install nfs-common (Ubuntu)

- NFS 서버에서 공유가능한 디렉토리 확인
showmount -e [nfs서버ip]

- NFS 서버에 마운트
mount -t nfs 서버ip:<공유할 디렉토리> <클라이언트에서 마운팅할 위치 즉, 마운팅포인트 - 절대경로>
sudo mount -t nfs 192.168.23.91:/volume1/nfs-node5 /mnt/c/Users/gocjs/0.capstone/nas_nfs

- 자동마운트
vi /etc/fstab
서버ip:/home/raw/heo_coin_data /home/raw/heo_coin_data nfs defaults 0.0(nfs계속연결시도)

- NFS 마운트 확인


#### <에러발생>
##### 1. mount.nfs: No such device
sudo mount -t nfs 192.168.23.91:/volume1/nfs-node5 /mnt/c/Users/gocjs/0.capstone/nas_nfs 
위의 커맨드 실행시 mount.nfs: No such device라는 에러 발생
##### 어떻게 해결할 것인가?





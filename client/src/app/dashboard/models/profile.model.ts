export interface UserProgileModel {
  trial: boolean;
}

export interface ProfileModel {
  userprofile: UserProgileModel;
  last_login: string;
  date_joined: string;
  is_superuser: boolean;
  username: string;
  is_active: boolean;
  sidemenu: any[];
}

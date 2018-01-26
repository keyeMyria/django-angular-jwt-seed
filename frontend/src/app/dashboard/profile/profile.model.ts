export class Owner {
  public last_login: string;
  public date_joined: string;
  public username = false;
}

export class UserProfile {
  public created: string;
  public modified: string;
  public owner: Owner;

}

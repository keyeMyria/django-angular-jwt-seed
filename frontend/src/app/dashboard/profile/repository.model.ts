import {Injectable} from '@angular/core';
import {ProfileRestDataSource} from './rest.datasource';
import {UserProfile} from './profile.model';

@Injectable()
export class Model {
  private profile: UserProfile;

  constructor(private dataSource: ProfileRestDataSource) {
    this.dataSource.getData().subscribe(
      (data: any) => {
        this.profile = data;
      }
    );
  }

  getProfile(): UserProfile {
    return this.profile;
  }
}

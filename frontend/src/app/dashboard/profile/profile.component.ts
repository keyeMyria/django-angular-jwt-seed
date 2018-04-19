import {Component} from '@angular/core';
import {ProfileRestDataSource} from './rest.datasource';
import {UserProfile} from './profile.model';

@Component({
  selector: 'app-profile-component',
  templateUrl: 'profile.component.html',
  styles: []
})
export class ProfileComponent {
  _userProfile: UserProfile;
  _error;

  constructor(public datasource: ProfileRestDataSource) {
    this.datasource.getData().subscribe(
      data => {
        this._userProfile = data;
      },
      error2 => {
        this._error = error2.toString();
      }
    );
  }
}

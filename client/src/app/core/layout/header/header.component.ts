import {Component} from '@angular/core';
import {AuthenticationService} from '../../../authentication/services/authentication.service';

import {Subscription} from 'rxjs/index';
import {ProfileModel, ProfileSourceService} from '../../../dashboard/';


@Component({
  selector: 'app-header-component',
  templateUrl: 'header.component.html'
})
export class HeaderComponent {
  profile: ProfileModel;

  subscription: Subscription;

  constructor(
    private _source: ProfileSourceService,
    private _authenticationService: AuthenticationService) {

    this.subscription = this._source.data$
      .subscribe((profile: ProfileModel) => this.profile = profile);

  }

  onLogOut(): void {
    this._authenticationService.logout();
  }

}

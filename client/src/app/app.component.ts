import {Component, OnDestroy, OnInit} from '@angular/core';

import '@clr/icons';
import '@clr/icons/shapes/all-shapes';
import {AuthenticationService} from './authentication/services/authentication.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';

  is_login: boolean;

  constructor(private _authService: AuthenticationService) {
    this._authService.isAuthorized().subscribe(frame => this.is_login = frame);
  }


  ngOnInit() {

  }

  ngOnDestroy() {
  }
}

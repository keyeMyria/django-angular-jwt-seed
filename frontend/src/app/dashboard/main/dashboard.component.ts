import {Component} from '@angular/core';
import {Router} from '@angular/router';
import {AuthenticationService} from '../../authentication';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent {

  constructor(private router: Router,
              private authService: AuthenticationService) {
  }

  public logout() {
    this.authService.logout();
    this.router.navigateByUrl('/');
  }

}
